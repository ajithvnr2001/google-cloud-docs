---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient
title: Managed Service for Apache Kafka API v1 API - Class ManagedKafkaClient (1.0.0-beta08) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:49.906058+00:00
---

# Managed Service for Apache Kafka API v1 API - Class ManagedKafkaClient (1.0.0-beta08)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Managed Service for Apache Kafka API v1 API - Class ManagedKafkaClient (1.0.0-beta08) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.0.0-beta08 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient)
  * [ 1.0.0-beta07 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/1.0.0-beta07/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient)


    
    
    public abstract class ManagedKafkaClient

Reference documentation and code samples for the Managed Service for Apache Kafka API v1 API class ManagedKafkaClient.

ManagedKafka client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ManagedKafkaClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ManagedKafkaClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClientImpl)

## Namespace

[Google.Cloud.ManagedKafka.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1)

## Assembly

Google.Cloud.ManagedKafka.V1.dll

## Remarks

The service that a client application uses to manage Apache Kafka clusters, topics and consumer groups.

## Properties 

### CreateClusterOperationsClient
    
    
    public virtual OperationsClient CreateClusterOperationsClient { get; }

The long-running operations client for `CreateCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ManagedKafka service, which is a host of "managedkafka.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ManagedKafka scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ManagedKafka scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteClusterOperationsClient
    
    
    public virtual OperationsClient DeleteClusterOperationsClient { get; }

The long-running operations client for `DeleteCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ManagedKafka.ManagedKafkaClient GrpcClient { get; }

The underlying gRPC ManagedKafka client

**Property Value**  
---  
**Type** | **Description**  
`[ManagedKafka](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafka)[ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafka.ManagedKafkaClient)` |   
  
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
  
### UpdateClusterOperationsClient
    
    
    public virtual OperationsClient UpdateClusterOperationsClient { get; }

The long-running operations client for `UpdateCluster`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
## Methods 

### AddAclEntry(AclName, AclEntry, CallSettings)
    
    
    public virtual AddAclEntryResponse AddAclEntry(AclName acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to add.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    AclName acl = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    AclEntry aclEntry = new AclEntry();
    // Make the request
    AddAclEntryResponse response = managedKafkaClient.AddAclEntry(acl, aclEntry);
    

### AddAclEntry(AddAclEntryRequest, CallSettings)
    
    
    public virtual AddAclEntryResponse AddAclEntry(AddAclEntryRequest request, CallSettings callSettings = null)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    AddAclEntryRequest request = new AddAclEntryRequest
    {
        AclAsAclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
        AclEntry = new AclEntry(),
    };
    // Make the request
    AddAclEntryResponse response = managedKafkaClient.AddAclEntry(request);
    

### AddAclEntry(string, AclEntry, CallSettings)
    
    
    public virtual AddAclEntryResponse AddAclEntry(string acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to add.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string acl = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    AclEntry aclEntry = new AclEntry();
    // Make the request
    AddAclEntryResponse response = managedKafkaClient.AddAclEntry(acl, aclEntry);
    

### AddAclEntryAsync(AclName, AclEntry, CallSettings)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntryAsync(AclName acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to add.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName acl = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    AclEntry aclEntry = new AclEntry();
    // Make the request
    AddAclEntryResponse response = await managedKafkaClient.AddAclEntryAsync(acl, aclEntry);
    

### AddAclEntryAsync(AclName, AclEntry, CancellationToken)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntryAsync(AclName acl, AclEntry aclEntry, CancellationToken cancellationToken)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to add.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName acl = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    AclEntry aclEntry = new AclEntry();
    // Make the request
    AddAclEntryResponse response = await managedKafkaClient.AddAclEntryAsync(acl, aclEntry);
    

### AddAclEntryAsync(AddAclEntryRequest, CallSettings)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntryAsync(AddAclEntryRequest request, CallSettings callSettings = null)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AddAclEntryRequest request = new AddAclEntryRequest
    {
        AclAsAclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
        AclEntry = new AclEntry(),
    };
    // Make the request
    AddAclEntryResponse response = await managedKafkaClient.AddAclEntryAsync(request);
    

### AddAclEntryAsync(AddAclEntryRequest, CancellationToken)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntryAsync(AddAclEntryRequest request, CancellationToken cancellationToken)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[AddAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AddAclEntryRequest request = new AddAclEntryRequest
    {
        AclAsAclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
        AclEntry = new AclEntry(),
    };
    // Make the request
    AddAclEntryResponse response = await managedKafkaClient.AddAclEntryAsync(request);
    

### AddAclEntryAsync(string, AclEntry, CallSettings)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntryAsync(string acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to add.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string acl = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    AclEntry aclEntry = new AclEntry();
    // Make the request
    AddAclEntryResponse response = await managedKafkaClient.AddAclEntryAsync(acl, aclEntry);
    

### AddAclEntryAsync(string, AclEntry, CancellationToken)
    
    
    public virtual Task<AddAclEntryResponse> AddAclEntryAsync(string acl, AclEntry aclEntry, CancellationToken cancellationToken)

Incremental update: Adds an acl entry to an acl. Creates the acl if it does not exist yet.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to add the acl entry to. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to add.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AddAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AddAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string acl = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    AclEntry aclEntry = new AclEntry();
    // Make the request
    AddAclEntryResponse response = await managedKafkaClient.AddAclEntryAsync(acl, aclEntry);
    

### Create()
    
    
    public static ManagedKafkaClient Create()

Synchronously creates a [ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ManagedKafkaClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient)` | The created [ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient).  
  
### CreateAcl(ClusterName, Acl, string, CallSettings)
    
    
    public virtual Acl CreateAcl(ClusterName parent, Acl acl, string aclId, CallSettings callSettings = null)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. Configuration of the acl to create. Its `name` field is ignored.  
`aclId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: For acls on the cluster: `cluster` For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}` For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}` For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Acl acl = new Acl();
    string aclId = "";
    // Make the request
    Acl response = managedKafkaClient.CreateAcl(parent, acl, aclId);
    

### CreateAcl(CreateAclRequest, CallSettings)
    
    
    public virtual Acl CreateAcl(CreateAclRequest request, CallSettings callSettings = null)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    CreateAclRequest request = new CreateAclRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        AclId = "",
        Acl = new Acl(),
    };
    // Make the request
    Acl response = managedKafkaClient.CreateAcl(request);
    

### CreateAcl(string, Acl, string, CallSettings)
    
    
    public virtual Acl CreateAcl(string parent, Acl acl, string aclId, CallSettings callSettings = null)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. Configuration of the acl to create. Its `name` field is ignored.  
`aclId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: For acls on the cluster: `cluster` For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}` For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}` For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Acl acl = new Acl();
    string aclId = "";
    // Make the request
    Acl response = managedKafkaClient.CreateAcl(parent, acl, aclId);
    

### CreateAclAsync(ClusterName, Acl, string, CallSettings)
    
    
    public virtual Task<Acl> CreateAclAsync(ClusterName parent, Acl acl, string aclId, CallSettings callSettings = null)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. Configuration of the acl to create. Its `name` field is ignored.  
`aclId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: For acls on the cluster: `cluster` For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}` For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}` For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Acl acl = new Acl();
    string aclId = "";
    // Make the request
    Acl response = await managedKafkaClient.CreateAclAsync(parent, acl, aclId);
    

### CreateAclAsync(ClusterName, Acl, string, CancellationToken)
    
    
    public virtual Task<Acl> CreateAclAsync(ClusterName parent, Acl acl, string aclId, CancellationToken cancellationToken)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. Configuration of the acl to create. Its `name` field is ignored.  
`aclId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: For acls on the cluster: `cluster` For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}` For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}` For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Acl acl = new Acl();
    string aclId = "";
    // Make the request
    Acl response = await managedKafkaClient.CreateAclAsync(parent, acl, aclId);
    

### CreateAclAsync(CreateAclRequest, CallSettings)
    
    
    public virtual Task<Acl> CreateAclAsync(CreateAclRequest request, CallSettings callSettings = null)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    CreateAclRequest request = new CreateAclRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        AclId = "",
        Acl = new Acl(),
    };
    // Make the request
    Acl response = await managedKafkaClient.CreateAclAsync(request);
    

### CreateAclAsync(CreateAclRequest, CancellationToken)
    
    
    public virtual Task<Acl> CreateAclAsync(CreateAclRequest request, CancellationToken cancellationToken)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateAclRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    CreateAclRequest request = new CreateAclRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        AclId = "",
        Acl = new Acl(),
    };
    // Make the request
    Acl response = await managedKafkaClient.CreateAclAsync(request);
    

### CreateAclAsync(string, Acl, string, CallSettings)
    
    
    public virtual Task<Acl> CreateAclAsync(string parent, Acl acl, string aclId, CallSettings callSettings = null)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. Configuration of the acl to create. Its `name` field is ignored.  
`aclId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: For acls on the cluster: `cluster` For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}` For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}` For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Acl acl = new Acl();
    string aclId = "";
    // Make the request
    Acl response = await managedKafkaClient.CreateAclAsync(parent, acl, aclId);
    

### CreateAclAsync(string, Acl, string, CancellationToken)
    
    
    public virtual Task<Acl> CreateAclAsync(string parent, Acl acl, string aclId, CancellationToken cancellationToken)

Creates a new acl in the given project, location, and cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster in which to create the acl. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. Configuration of the acl to create. Its `name` field is ignored.  
`aclId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the acl, which will become the final component of the acl's name. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. `acl_id` is structured like one of the following: For acls on the cluster: `cluster` For acls on a single resource within the cluster: `topic/{resource_name}` `consumerGroup/{resource_name}` `transactionalId/{resource_name}` For acls on all resources that match a prefix: `topicPrefixed/{resource_name}` `consumerGroupPrefixed/{resource_name}` `transactionalIdPrefixed/{resource_name}` For acls on all resources of a given type (i.e. the wildcard literal "_"):`allTopics` (represents `topic/_`)`allConsumerGroups`(represents`consumerGroup/_`)`allTransactionalIds`(represents`transactionalId/_`)  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Acl acl = new Acl();
    string aclId = "";
    // Make the request
    Acl response = await managedKafkaClient.CreateAclAsync(parent, acl, aclId);
    

### CreateAsync(CancellationToken)
    
    
    public static Task<ManagedKafkaClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ManagedKafkaClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient)` | The task representing the created [ManagedKafkaClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient).  
  
### CreateCluster(LocationName, Cluster, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateCluster(LocationName parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent region in which to create the cluster. Structured like `projects/{project}/locations/{location}`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. Configuration of the cluster to create. Its `name` field is ignored.  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = managedKafkaClient.CreateCluster(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceCreateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateCluster(CreateClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateCluster(CreateClusterRequest request, CallSettings callSettings = null)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = managedKafkaClient.CreateCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceCreateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateCluster(string, Cluster, string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> CreateCluster(string parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent region in which to create the cluster. Structured like `projects/{project}/locations/{location}`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. Configuration of the cluster to create. Its `name` field is ignored.  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = managedKafkaClient.CreateCluster(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceCreateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(LocationName, Cluster, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(LocationName parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent region in which to create the cluster. Structured like `projects/{project}/locations/{location}`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. Configuration of the cluster to create. Its `name` field is ignored.  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(LocationName, Cluster, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(LocationName parent, Cluster cluster, string clusterId, CancellationToken cancellationToken)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent region in which to create the cluster. Structured like `projects/{project}/locations/{location}`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. Configuration of the cluster to create. Its `name` field is ignored.  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(CreateClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(CreateClusterRequest request, CallSettings callSettings = null)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.CreateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(CreateClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(CreateClusterRequest request, CancellationToken cancellationToken)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    CreateClusterRequest request = new CreateClusterRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ClusterId = "",
        Cluster = new Cluster(),
        RequestId = "",
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.CreateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(string, Cluster, string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(string parent, Cluster cluster, string clusterId, CallSettings callSettings = null)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent region in which to create the cluster. Structured like `projects/{project}/locations/{location}`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. Configuration of the cluster to create. Its `name` field is ignored.  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateClusterAsync(string, Cluster, string, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> CreateClusterAsync(string parent, Cluster cluster, string clusterId, CancellationToken cancellationToken)

Creates a new cluster in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent region in which to create the cluster. Structured like `projects/{project}/locations/{location}`.  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. Configuration of the cluster to create. Its `name` field is ignored.  
`clusterId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the cluster, which will become the final component of the cluster's name. The ID must be 1-63 characters long, and match the regular expression `[a-z]([-a-z0-9]*[a-z0-9])?` to comply with RFC 1035. This value is structured like: `my-cluster-id`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Cluster cluster = new Cluster();
    string clusterId = "";
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.CreateClusterAsync(parent, cluster, clusterId);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceCreateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### CreateTopic(ClusterName, Topic, string, CallSettings)
    
    
    public virtual Topic CreateTopic(ClusterName parent, Topic topic, string topicId, CallSettings callSettings = null)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster in which to create the topic. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. Configuration of the topic to create. Its `name` field is ignored.  
`topicId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the topic, which will become the final component of the topic's name. This value is structured like: `my-topic-name`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Topic topic = new Topic();
    string topicId = "";
    // Make the request
    Topic response = managedKafkaClient.CreateTopic(parent, topic, topicId);
    

### CreateTopic(CreateTopicRequest, CallSettings)
    
    
    public virtual Topic CreateTopic(CreateTopicRequest request, CallSettings callSettings = null)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    CreateTopicRequest request = new CreateTopicRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        TopicId = "",
        Topic = new Topic(),
    };
    // Make the request
    Topic response = managedKafkaClient.CreateTopic(request);
    

### CreateTopic(string, Topic, string, CallSettings)
    
    
    public virtual Topic CreateTopic(string parent, Topic topic, string topicId, CallSettings callSettings = null)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster in which to create the topic. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. Configuration of the topic to create. Its `name` field is ignored.  
`topicId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the topic, which will become the final component of the topic's name. This value is structured like: `my-topic-name`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Topic topic = new Topic();
    string topicId = "";
    // Make the request
    Topic response = managedKafkaClient.CreateTopic(parent, topic, topicId);
    

### CreateTopicAsync(ClusterName, Topic, string, CallSettings)
    
    
    public virtual Task<Topic> CreateTopicAsync(ClusterName parent, Topic topic, string topicId, CallSettings callSettings = null)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster in which to create the topic. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. Configuration of the topic to create. Its `name` field is ignored.  
`topicId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the topic, which will become the final component of the topic's name. This value is structured like: `my-topic-name`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Topic topic = new Topic();
    string topicId = "";
    // Make the request
    Topic response = await managedKafkaClient.CreateTopicAsync(parent, topic, topicId);
    

### CreateTopicAsync(ClusterName, Topic, string, CancellationToken)
    
    
    public virtual Task<Topic> CreateTopicAsync(ClusterName parent, Topic topic, string topicId, CancellationToken cancellationToken)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster in which to create the topic. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. Configuration of the topic to create. Its `name` field is ignored.  
`topicId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the topic, which will become the final component of the topic's name. This value is structured like: `my-topic-name`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    Topic topic = new Topic();
    string topicId = "";
    // Make the request
    Topic response = await managedKafkaClient.CreateTopicAsync(parent, topic, topicId);
    

### CreateTopicAsync(CreateTopicRequest, CallSettings)
    
    
    public virtual Task<Topic> CreateTopicAsync(CreateTopicRequest request, CallSettings callSettings = null)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    CreateTopicRequest request = new CreateTopicRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        TopicId = "",
        Topic = new Topic(),
    };
    // Make the request
    Topic response = await managedKafkaClient.CreateTopicAsync(request);
    

### CreateTopicAsync(CreateTopicRequest, CancellationToken)
    
    
    public virtual Task<Topic> CreateTopicAsync(CreateTopicRequest request, CancellationToken cancellationToken)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.CreateTopicRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    CreateTopicRequest request = new CreateTopicRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        TopicId = "",
        Topic = new Topic(),
    };
    // Make the request
    Topic response = await managedKafkaClient.CreateTopicAsync(request);
    

### CreateTopicAsync(string, Topic, string, CallSettings)
    
    
    public virtual Task<Topic> CreateTopicAsync(string parent, Topic topic, string topicId, CallSettings callSettings = null)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster in which to create the topic. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. Configuration of the topic to create. Its `name` field is ignored.  
`topicId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the topic, which will become the final component of the topic's name. This value is structured like: `my-topic-name`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Topic topic = new Topic();
    string topicId = "";
    // Make the request
    Topic response = await managedKafkaClient.CreateTopicAsync(parent, topic, topicId);
    

### CreateTopicAsync(string, Topic, string, CancellationToken)
    
    
    public virtual Task<Topic> CreateTopicAsync(string parent, Topic topic, string topicId, CancellationToken cancellationToken)

Creates a new topic in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster in which to create the topic. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. Configuration of the topic to create. Its `name` field is ignored.  
`topicId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the topic, which will become the final component of the topic's name. This value is structured like: `my-topic-name`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    Topic topic = new Topic();
    string topicId = "";
    // Make the request
    Topic response = await managedKafkaClient.CreateTopicAsync(parent, topic, topicId);
    

### DeleteAcl(AclName, CallSettings)
    
    
    public virtual void DeleteAcl(AclName name, CallSettings callSettings = null)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    AclName name = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    // Make the request
    managedKafkaClient.DeleteAcl(name);
    

### DeleteAcl(DeleteAclRequest, CallSettings)
    
    
    public virtual void DeleteAcl(DeleteAclRequest request, CallSettings callSettings = null)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    DeleteAclRequest request = new DeleteAclRequest
    {
        AclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
    };
    // Make the request
    managedKafkaClient.DeleteAcl(request);
    

### DeleteAcl(string, CallSettings)
    
    
    public virtual void DeleteAcl(string name, CallSettings callSettings = null)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    // Make the request
    managedKafkaClient.DeleteAcl(name);
    

### DeleteAclAsync(AclName, CallSettings)
    
    
    public virtual Task DeleteAclAsync(AclName name, CallSettings callSettings = null)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName name = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    // Make the request
    await managedKafkaClient.DeleteAclAsync(name);
    

### DeleteAclAsync(AclName, CancellationToken)
    
    
    public virtual Task DeleteAclAsync(AclName name, CancellationToken cancellationToken)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName name = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    // Make the request
    await managedKafkaClient.DeleteAclAsync(name);
    

### DeleteAclAsync(DeleteAclRequest, CallSettings)
    
    
    public virtual Task DeleteAclAsync(DeleteAclRequest request, CallSettings callSettings = null)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAclRequest request = new DeleteAclRequest
    {
        AclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
    };
    // Make the request
    await managedKafkaClient.DeleteAclAsync(request);
    

### DeleteAclAsync(DeleteAclRequest, CancellationToken)
    
    
    public virtual Task DeleteAclAsync(DeleteAclRequest request, CancellationToken cancellationToken)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteAclRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteAclRequest request = new DeleteAclRequest
    {
        AclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
    };
    // Make the request
    await managedKafkaClient.DeleteAclAsync(request);
    

### DeleteAclAsync(string, CallSettings)
    
    
    public virtual Task DeleteAclAsync(string name, CallSettings callSettings = null)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    // Make the request
    await managedKafkaClient.DeleteAclAsync(name);
    

### DeleteAclAsync(string, CancellationToken)
    
    
    public virtual Task DeleteAclAsync(string name, CancellationToken cancellationToken)

Deletes an acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to delete. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    // Make the request
    await managedKafkaClient.DeleteAclAsync(name);
    

### DeleteCluster(ClusterName, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteCluster(ClusterName name, CallSettings callSettings = null)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The name of the cluster to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = managedKafkaClient.DeleteCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceDeleteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCluster(DeleteClusterRequest, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteCluster(DeleteClusterRequest request, CallSettings callSettings = null)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = managedKafkaClient.DeleteCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceDeleteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteCluster(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> DeleteCluster(string name, CallSettings callSettings = null)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the cluster to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = managedKafkaClient.DeleteCluster(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceDeleteCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(ClusterName, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(ClusterName name, CallSettings callSettings = null)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The name of the cluster to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(ClusterName name, CancellationToken cancellationToken)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The name of the cluster to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(DeleteClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(DeleteClusterRequest request, CallSettings callSettings = null)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaClient.DeleteClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(DeleteClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(DeleteClusterRequest request, CancellationToken cancellationToken)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteClusterRequest request = new DeleteClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
        RequestId = "",
    };
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaClient.DeleteClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(string name, CallSettings callSettings = null)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the cluster to delete.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> DeleteClusterAsync(string name, CancellationToken cancellationToken)

Deletes a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the cluster to delete.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Operation<Empty, OperationMetadata> response = await managedKafkaClient.DeleteClusterAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceDeleteClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteConsumerGroup(ConsumerGroupName, CallSettings)
    
    
    public virtual void DeleteConsumerGroup(ConsumerGroupName name, CallSettings callSettings = null)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConsumerGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroupName)`  
Required. The name of the consumer group to delete. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ConsumerGroupName name = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]");
    // Make the request
    managedKafkaClient.DeleteConsumerGroup(name);
    

### DeleteConsumerGroup(DeleteConsumerGroupRequest, CallSettings)
    
    
    public virtual void DeleteConsumerGroup(DeleteConsumerGroupRequest request, CallSettings callSettings = null)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    DeleteConsumerGroupRequest request = new DeleteConsumerGroupRequest
    {
        ConsumerGroupName = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]"),
    };
    // Make the request
    managedKafkaClient.DeleteConsumerGroup(request);
    

### DeleteConsumerGroup(string, CallSettings)
    
    
    public virtual void DeleteConsumerGroup(string name, CallSettings callSettings = null)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the consumer group to delete. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/consumerGroups/[CONSUMER_GROUP]";
    // Make the request
    managedKafkaClient.DeleteConsumerGroup(name);
    

### DeleteConsumerGroupAsync(ConsumerGroupName, CallSettings)
    
    
    public virtual Task DeleteConsumerGroupAsync(ConsumerGroupName name, CallSettings callSettings = null)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConsumerGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroupName)`  
Required. The name of the consumer group to delete. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ConsumerGroupName name = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]");
    // Make the request
    await managedKafkaClient.DeleteConsumerGroupAsync(name);
    

### DeleteConsumerGroupAsync(ConsumerGroupName, CancellationToken)
    
    
    public virtual Task DeleteConsumerGroupAsync(ConsumerGroupName name, CancellationToken cancellationToken)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConsumerGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroupName)`  
Required. The name of the consumer group to delete. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ConsumerGroupName name = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]");
    // Make the request
    await managedKafkaClient.DeleteConsumerGroupAsync(name);
    

### DeleteConsumerGroupAsync(DeleteConsumerGroupRequest, CallSettings)
    
    
    public virtual Task DeleteConsumerGroupAsync(DeleteConsumerGroupRequest request, CallSettings callSettings = null)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConsumerGroupRequest request = new DeleteConsumerGroupRequest
    {
        ConsumerGroupName = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]"),
    };
    // Make the request
    await managedKafkaClient.DeleteConsumerGroupAsync(request);
    

### DeleteConsumerGroupAsync(DeleteConsumerGroupRequest, CancellationToken)
    
    
    public virtual Task DeleteConsumerGroupAsync(DeleteConsumerGroupRequest request, CancellationToken cancellationToken)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteConsumerGroupRequest request = new DeleteConsumerGroupRequest
    {
        ConsumerGroupName = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]"),
    };
    // Make the request
    await managedKafkaClient.DeleteConsumerGroupAsync(request);
    

### DeleteConsumerGroupAsync(string, CallSettings)
    
    
    public virtual Task DeleteConsumerGroupAsync(string name, CallSettings callSettings = null)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the consumer group to delete. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/consumerGroups/[CONSUMER_GROUP]";
    // Make the request
    await managedKafkaClient.DeleteConsumerGroupAsync(name);
    

### DeleteConsumerGroupAsync(string, CancellationToken)
    
    
    public virtual Task DeleteConsumerGroupAsync(string name, CancellationToken cancellationToken)

Deletes a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the consumer group to delete. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/consumerGroups/[CONSUMER_GROUP]";
    // Make the request
    await managedKafkaClient.DeleteConsumerGroupAsync(name);
    

### DeleteTopic(DeleteTopicRequest, CallSettings)
    
    
    public virtual void DeleteTopic(DeleteTopicRequest request, CallSettings callSettings = null)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    DeleteTopicRequest request = new DeleteTopicRequest
    {
        TopicName = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]"),
    };
    // Make the request
    managedKafkaClient.DeleteTopic(request);
    

### DeleteTopic(TopicName, CallSettings)
    
    
    public virtual void DeleteTopic(TopicName name, CallSettings callSettings = null)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TopicName)`  
Required. The name of the topic to delete. `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    TopicName name = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]");
    // Make the request
    managedKafkaClient.DeleteTopic(name);
    

### DeleteTopic(string, CallSettings)
    
    
    public virtual void DeleteTopic(string name, CallSettings callSettings = null)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the topic to delete. `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/topics/[TOPIC]";
    // Make the request
    managedKafkaClient.DeleteTopic(name);
    

### DeleteTopicAsync(DeleteTopicRequest, CallSettings)
    
    
    public virtual Task DeleteTopicAsync(DeleteTopicRequest request, CallSettings callSettings = null)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteTopicRequest request = new DeleteTopicRequest
    {
        TopicName = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]"),
    };
    // Make the request
    await managedKafkaClient.DeleteTopicAsync(request);
    

### DeleteTopicAsync(DeleteTopicRequest, CancellationToken)
    
    
    public virtual Task DeleteTopicAsync(DeleteTopicRequest request, CancellationToken cancellationToken)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.DeleteTopicRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    DeleteTopicRequest request = new DeleteTopicRequest
    {
        TopicName = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]"),
    };
    // Make the request
    await managedKafkaClient.DeleteTopicAsync(request);
    

### DeleteTopicAsync(TopicName, CallSettings)
    
    
    public virtual Task DeleteTopicAsync(TopicName name, CallSettings callSettings = null)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TopicName)`  
Required. The name of the topic to delete. `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    TopicName name = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]");
    // Make the request
    await managedKafkaClient.DeleteTopicAsync(name);
    

### DeleteTopicAsync(TopicName, CancellationToken)
    
    
    public virtual Task DeleteTopicAsync(TopicName name, CancellationToken cancellationToken)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TopicName)`  
Required. The name of the topic to delete. `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    TopicName name = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]");
    // Make the request
    await managedKafkaClient.DeleteTopicAsync(name);
    

### DeleteTopicAsync(string, CallSettings)
    
    
    public virtual Task DeleteTopicAsync(string name, CallSettings callSettings = null)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the topic to delete. `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/topics/[TOPIC]";
    // Make the request
    await managedKafkaClient.DeleteTopicAsync(name);
    

### DeleteTopicAsync(string, CancellationToken)
    
    
    public virtual Task DeleteTopicAsync(string name, CancellationToken cancellationToken)

Deletes a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the topic to delete. `projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/topics/[TOPIC]";
    // Make the request
    await managedKafkaClient.DeleteTopicAsync(name);
    

### GetAcl(AclName, CallSettings)
    
    
    public virtual Acl GetAcl(AclName name, CallSettings callSettings = null)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to return. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    AclName name = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    // Make the request
    Acl response = managedKafkaClient.GetAcl(name);
    

### GetAcl(GetAclRequest, CallSettings)
    
    
    public virtual Acl GetAcl(GetAclRequest request, CallSettings callSettings = null)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    GetAclRequest request = new GetAclRequest
    {
        AclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
    };
    // Make the request
    Acl response = managedKafkaClient.GetAcl(request);
    

### GetAcl(string, CallSettings)
    
    
    public virtual Acl GetAcl(string name, CallSettings callSettings = null)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to return. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    // Make the request
    Acl response = managedKafkaClient.GetAcl(name);
    

### GetAclAsync(AclName, CallSettings)
    
    
    public virtual Task<Acl> GetAclAsync(AclName name, CallSettings callSettings = null)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to return. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName name = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    // Make the request
    Acl response = await managedKafkaClient.GetAclAsync(name);
    

### GetAclAsync(AclName, CancellationToken)
    
    
    public virtual Task<Acl> GetAclAsync(AclName name, CancellationToken cancellationToken)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to return. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName name = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    // Make the request
    Acl response = await managedKafkaClient.GetAclAsync(name);
    

### GetAclAsync(GetAclRequest, CallSettings)
    
    
    public virtual Task<Acl> GetAclAsync(GetAclRequest request, CallSettings callSettings = null)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetAclRequest request = new GetAclRequest
    {
        AclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
    };
    // Make the request
    Acl response = await managedKafkaClient.GetAclAsync(request);
    

### GetAclAsync(GetAclRequest, CancellationToken)
    
    
    public virtual Task<Acl> GetAclAsync(GetAclRequest request, CancellationToken cancellationToken)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetAclRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetAclRequest request = new GetAclRequest
    {
        AclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
    };
    // Make the request
    Acl response = await managedKafkaClient.GetAclAsync(request);
    

### GetAclAsync(string, CallSettings)
    
    
    public virtual Task<Acl> GetAclAsync(string name, CallSettings callSettings = null)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to return. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    // Make the request
    Acl response = await managedKafkaClient.GetAclAsync(name);
    

### GetAclAsync(string, CancellationToken)
    
    
    public virtual Task<Acl> GetAclAsync(string name, CancellationToken cancellationToken)

Returns the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to return. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    // Make the request
    Acl response = await managedKafkaClient.GetAclAsync(name);
    

### GetCluster(ClusterName, CallSettings)
    
    
    public virtual Cluster GetCluster(ClusterName name, CallSettings callSettings = null)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The name of the cluster whose configuration to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Cluster response = managedKafkaClient.GetCluster(name);
    

### GetCluster(GetClusterRequest, CallSettings)
    
    
    public virtual Cluster GetCluster(GetClusterRequest request, CallSettings callSettings = null)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    GetClusterRequest request = new GetClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    Cluster response = managedKafkaClient.GetCluster(request);
    

### GetCluster(string, CallSettings)
    
    
    public virtual Cluster GetCluster(string name, CallSettings callSettings = null)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the cluster whose configuration to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Cluster response = managedKafkaClient.GetCluster(name);
    

### GetClusterAsync(ClusterName, CallSettings)
    
    
    public virtual Task<Cluster> GetClusterAsync(ClusterName name, CallSettings callSettings = null)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The name of the cluster whose configuration to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Cluster response = await managedKafkaClient.GetClusterAsync(name);
    

### GetClusterAsync(ClusterName, CancellationToken)
    
    
    public virtual Task<Cluster> GetClusterAsync(ClusterName name, CancellationToken cancellationToken)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The name of the cluster whose configuration to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName name = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    Cluster response = await managedKafkaClient.GetClusterAsync(name);
    

### GetClusterAsync(GetClusterRequest, CallSettings)
    
    
    public virtual Task<Cluster> GetClusterAsync(GetClusterRequest request, CallSettings callSettings = null)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetClusterRequest request = new GetClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    Cluster response = await managedKafkaClient.GetClusterAsync(request);
    

### GetClusterAsync(GetClusterRequest, CancellationToken)
    
    
    public virtual Task<Cluster> GetClusterAsync(GetClusterRequest request, CancellationToken cancellationToken)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetClusterRequest request = new GetClusterRequest
    {
        ClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    Cluster response = await managedKafkaClient.GetClusterAsync(request);
    

### GetClusterAsync(string, CallSettings)
    
    
    public virtual Task<Cluster> GetClusterAsync(string name, CallSettings callSettings = null)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the cluster whose configuration to return.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Cluster response = await managedKafkaClient.GetClusterAsync(name);
    

### GetClusterAsync(string, CancellationToken)
    
    
    public virtual Task<Cluster> GetClusterAsync(string name, CancellationToken cancellationToken)

Returns the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the cluster whose configuration to return.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    Cluster response = await managedKafkaClient.GetClusterAsync(name);
    

### GetConsumerGroup(ConsumerGroupName, CallSettings)
    
    
    public virtual ConsumerGroup GetConsumerGroup(ConsumerGroupName name, CallSettings callSettings = null)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConsumerGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroupName)`  
Required. The name of the consumer group whose configuration to return. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ConsumerGroupName name = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]");
    // Make the request
    ConsumerGroup response = managedKafkaClient.GetConsumerGroup(name);
    

### GetConsumerGroup(GetConsumerGroupRequest, CallSettings)
    
    
    public virtual ConsumerGroup GetConsumerGroup(GetConsumerGroupRequest request, CallSettings callSettings = null)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    GetConsumerGroupRequest request = new GetConsumerGroupRequest
    {
        ConsumerGroupName = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]"),
    };
    // Make the request
    ConsumerGroup response = managedKafkaClient.GetConsumerGroup(request);
    

### GetConsumerGroup(string, CallSettings)
    
    
    public virtual ConsumerGroup GetConsumerGroup(string name, CallSettings callSettings = null)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the consumer group whose configuration to return. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/consumerGroups/[CONSUMER_GROUP]";
    // Make the request
    ConsumerGroup response = managedKafkaClient.GetConsumerGroup(name);
    

### GetConsumerGroupAsync(ConsumerGroupName, CallSettings)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroupAsync(ConsumerGroupName name, CallSettings callSettings = null)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConsumerGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroupName)`  
Required. The name of the consumer group whose configuration to return. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ConsumerGroupName name = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]");
    // Make the request
    ConsumerGroup response = await managedKafkaClient.GetConsumerGroupAsync(name);
    

### GetConsumerGroupAsync(ConsumerGroupName, CancellationToken)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroupAsync(ConsumerGroupName name, CancellationToken cancellationToken)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConsumerGroupName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroupName)`  
Required. The name of the consumer group whose configuration to return. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ConsumerGroupName name = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]");
    // Make the request
    ConsumerGroup response = await managedKafkaClient.GetConsumerGroupAsync(name);
    

### GetConsumerGroupAsync(GetConsumerGroupRequest, CallSettings)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroupAsync(GetConsumerGroupRequest request, CallSettings callSettings = null)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetConsumerGroupRequest request = new GetConsumerGroupRequest
    {
        ConsumerGroupName = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]"),
    };
    // Make the request
    ConsumerGroup response = await managedKafkaClient.GetConsumerGroupAsync(request);
    

### GetConsumerGroupAsync(GetConsumerGroupRequest, CancellationToken)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroupAsync(GetConsumerGroupRequest request, CancellationToken cancellationToken)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetConsumerGroupRequest request = new GetConsumerGroupRequest
    {
        ConsumerGroupName = ConsumerGroupName.FromProjectLocationClusterConsumerGroup("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[CONSUMER_GROUP]"),
    };
    // Make the request
    ConsumerGroup response = await managedKafkaClient.GetConsumerGroupAsync(request);
    

### GetConsumerGroupAsync(string, CallSettings)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroupAsync(string name, CallSettings callSettings = null)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the consumer group whose configuration to return. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/consumerGroups/[CONSUMER_GROUP]";
    // Make the request
    ConsumerGroup response = await managedKafkaClient.GetConsumerGroupAsync(name);
    

### GetConsumerGroupAsync(string, CancellationToken)
    
    
    public virtual Task<ConsumerGroup> GetConsumerGroupAsync(string name, CancellationToken cancellationToken)

Returns the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the consumer group whose configuration to return. `projects/{project}/locations/{location}/clusters/{cluster}/consumerGroups/{consumerGroup}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/consumerGroups/[CONSUMER_GROUP]";
    // Make the request
    ConsumerGroup response = await managedKafkaClient.GetConsumerGroupAsync(name);
    

### GetTopic(GetTopicRequest, CallSettings)
    
    
    public virtual Topic GetTopic(GetTopicRequest request, CallSettings callSettings = null)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    GetTopicRequest request = new GetTopicRequest
    {
        TopicName = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]"),
    };
    // Make the request
    Topic response = managedKafkaClient.GetTopic(request);
    

### GetTopic(TopicName, CallSettings)
    
    
    public virtual Topic GetTopic(TopicName name, CallSettings callSettings = null)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TopicName)`  
Required. The name of the topic whose configuration to return. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    TopicName name = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]");
    // Make the request
    Topic response = managedKafkaClient.GetTopic(name);
    

### GetTopic(string, CallSettings)
    
    
    public virtual Topic GetTopic(string name, CallSettings callSettings = null)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the topic whose configuration to return. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/topics/[TOPIC]";
    // Make the request
    Topic response = managedKafkaClient.GetTopic(name);
    

### GetTopicAsync(GetTopicRequest, CallSettings)
    
    
    public virtual Task<Topic> GetTopicAsync(GetTopicRequest request, CallSettings callSettings = null)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetTopicRequest request = new GetTopicRequest
    {
        TopicName = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]"),
    };
    // Make the request
    Topic response = await managedKafkaClient.GetTopicAsync(request);
    

### GetTopicAsync(GetTopicRequest, CancellationToken)
    
    
    public virtual Task<Topic> GetTopicAsync(GetTopicRequest request, CancellationToken cancellationToken)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.GetTopicRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    GetTopicRequest request = new GetTopicRequest
    {
        TopicName = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]"),
    };
    // Make the request
    Topic response = await managedKafkaClient.GetTopicAsync(request);
    

### GetTopicAsync(TopicName, CallSettings)
    
    
    public virtual Task<Topic> GetTopicAsync(TopicName name, CallSettings callSettings = null)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TopicName)`  
Required. The name of the topic whose configuration to return. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    TopicName name = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]");
    // Make the request
    Topic response = await managedKafkaClient.GetTopicAsync(name);
    

### GetTopicAsync(TopicName, CancellationToken)
    
    
    public virtual Task<Topic> GetTopicAsync(TopicName name, CancellationToken cancellationToken)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[TopicName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.TopicName)`  
Required. The name of the topic whose configuration to return. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    TopicName name = TopicName.FromProjectLocationClusterTopic("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[TOPIC]");
    // Make the request
    Topic response = await managedKafkaClient.GetTopicAsync(name);
    

### GetTopicAsync(string, CallSettings)
    
    
    public virtual Task<Topic> GetTopicAsync(string name, CallSettings callSettings = null)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the topic whose configuration to return. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/topics/[TOPIC]";
    // Make the request
    Topic response = await managedKafkaClient.GetTopicAsync(name);
    

### GetTopicAsync(string, CancellationToken)
    
    
    public virtual Task<Topic> GetTopicAsync(string name, CancellationToken cancellationToken)

Returns the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the topic whose configuration to return. Structured like: projects/{project}/locations/{location}/clusters/{cluster}/topics/{topic}.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/topics/[TOPIC]";
    // Make the request
    Topic response = await managedKafkaClient.GetTopicAsync(name);
    

### ListAcls(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAclsResponse, Acl> ListAcls(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster whose acls are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A pageable sequence of [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedEnumerable<ListAclsResponse, Acl> response = managedKafkaClient.ListAcls(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Acl item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAclsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Acl item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Acl> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Acl item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAcls(ListAclsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListAclsResponse, Acl> ListAcls(ListAclsRequest request, CallSettings callSettings = null)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A pageable sequence of [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ListAclsRequest request = new ListAclsRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    PagedEnumerable<ListAclsResponse, Acl> response = managedKafkaClient.ListAcls(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Acl item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAclsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Acl item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Acl> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Acl item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAcls(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListAclsResponse, Acl> ListAcls(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster whose acls are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A pageable sequence of [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedEnumerable<ListAclsResponse, Acl> response = managedKafkaClient.ListAcls(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Acl item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListAclsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Acl item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Acl> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Acl item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAclsAsync(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAclsResponse, Acl> ListAclsAsync(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster whose acls are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A pageable asynchronous sequence of [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListAclsResponse, Acl> response = managedKafkaClient.ListAclsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Acl item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListAclsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Acl item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Acl> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Acl item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAclsAsync(ListAclsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAclsResponse, Acl> ListAclsAsync(ListAclsRequest request, CallSettings callSettings = null)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListAclsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A pageable asynchronous sequence of [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ListAclsRequest request = new ListAclsRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListAclsResponse, Acl> response = managedKafkaClient.ListAclsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Acl item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListAclsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Acl item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Acl> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Acl item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListAclsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListAclsResponse, Acl> ListAclsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the acls in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster whose acls are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListAclsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListAclsResponse)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A pageable asynchronous sequence of [Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListAclsResponse, Acl> response = managedKafkaClient.ListAclsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Acl item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListAclsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Acl item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Acl> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Acl item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClusters(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListClustersResponse, Cluster> ListClusters(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent location whose clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A pageable sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListClustersResponse, Cluster> response = managedKafkaClient.ListClusters(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClusters(ListClustersRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListClustersResponse, Cluster> ListClusters(ListClustersRequest request, CallSettings callSettings = null)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A pageable sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ListClustersRequest request = new ListClustersRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListClustersResponse, Cluster> response = managedKafkaClient.ListClusters(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClusters(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListClustersResponse, Cluster> ListClusters(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent location whose clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A pageable sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListClustersResponse, Cluster> response = managedKafkaClient.ListClusters(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Cluster item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListClustersResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClustersAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListClustersResponse, Cluster> ListClustersAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent location whose clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A pageable asynchronous sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListClustersResponse, Cluster> response = managedKafkaClient.ListClustersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Cluster item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListClustersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClustersAsync(ListClustersRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListClustersResponse, Cluster> ListClustersAsync(ListClustersRequest request, CallSettings callSettings = null)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListClustersRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A pageable asynchronous sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ListClustersRequest request = new ListClustersRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListClustersResponse, Cluster> response = managedKafkaClient.ListClustersAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Cluster item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListClustersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListClustersAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListClustersResponse, Cluster> ListClustersAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the clusters in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent location whose clusters are to be listed. Structured like `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListClustersResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListClustersResponse)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)` | A pageable asynchronous sequence of [Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListClustersResponse, Cluster> response = managedKafkaClient.ListClustersAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Cluster item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListClustersResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Cluster item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Cluster> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Cluster item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConsumerGroups(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConsumerGroupsResponse, ConsumerGroup> ListConsumerGroups(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster whose consumer groups are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A pageable sequence of [ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedEnumerable<ListConsumerGroupsResponse, ConsumerGroup> response = managedKafkaClient.ListConsumerGroups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConsumerGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConsumerGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConsumerGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConsumerGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConsumerGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConsumerGroups(ListConsumerGroupsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConsumerGroupsResponse, ConsumerGroup> ListConsumerGroups(ListConsumerGroupsRequest request, CallSettings callSettings = null)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConsumerGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A pageable sequence of [ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ListConsumerGroupsRequest request = new ListConsumerGroupsRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    PagedEnumerable<ListConsumerGroupsResponse, ConsumerGroup> response = managedKafkaClient.ListConsumerGroups(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConsumerGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConsumerGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConsumerGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConsumerGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConsumerGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConsumerGroups(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConsumerGroupsResponse, ConsumerGroup> ListConsumerGroups(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster whose consumer groups are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A pageable sequence of [ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedEnumerable<ListConsumerGroupsResponse, ConsumerGroup> response = managedKafkaClient.ListConsumerGroups(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ConsumerGroup item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConsumerGroupsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConsumerGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConsumerGroup> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConsumerGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConsumerGroupsAsync(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConsumerGroupsResponse, ConsumerGroup> ListConsumerGroupsAsync(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster whose consumer groups are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A pageable asynchronous sequence of [ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListConsumerGroupsResponse, ConsumerGroup> response = managedKafkaClient.ListConsumerGroupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConsumerGroup item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConsumerGroupsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConsumerGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConsumerGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConsumerGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConsumerGroupsAsync(ListConsumerGroupsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConsumerGroupsResponse, ConsumerGroup> ListConsumerGroupsAsync(ListConsumerGroupsRequest request, CallSettings callSettings = null)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConsumerGroupsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A pageable asynchronous sequence of [ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ListConsumerGroupsRequest request = new ListConsumerGroupsRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListConsumerGroupsResponse, ConsumerGroup> response = managedKafkaClient.ListConsumerGroupsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConsumerGroup item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConsumerGroupsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConsumerGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConsumerGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConsumerGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConsumerGroupsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConsumerGroupsResponse, ConsumerGroup> ListConsumerGroupsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the consumer groups in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster whose consumer groups are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConsumerGroupsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListConsumerGroupsResponse)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A pageable asynchronous sequence of [ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListConsumerGroupsResponse, ConsumerGroup> response = managedKafkaClient.ListConsumerGroupsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((ConsumerGroup item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListConsumerGroupsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ConsumerGroup item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ConsumerGroup> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ConsumerGroup item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTopics(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTopicsResponse, Topic> ListTopics(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster whose topics are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A pageable sequence of [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedEnumerable<ListTopicsResponse, Topic> response = managedKafkaClient.ListTopics(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Topic item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTopicsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Topic item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Topic> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Topic item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTopics(ListTopicsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListTopicsResponse, Topic> ListTopics(ListTopicsRequest request, CallSettings callSettings = null)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A pageable sequence of [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ListTopicsRequest request = new ListTopicsRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    PagedEnumerable<ListTopicsResponse, Topic> response = managedKafkaClient.ListTopics(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Topic item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTopicsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Topic item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Topic> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Topic item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTopics(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListTopicsResponse, Topic> ListTopics(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster whose topics are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A pageable sequence of [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedEnumerable<ListTopicsResponse, Topic> response = managedKafkaClient.ListTopics(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Topic item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListTopicsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Topic item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Topic> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Topic item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTopicsAsync(ClusterName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTopicsResponse, Topic> ListTopicsAsync(ClusterName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ClusterName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ClusterName)`  
Required. The parent cluster whose topics are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A pageable asynchronous sequence of [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ClusterName parent = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]");
    // Make the request
    PagedAsyncEnumerable<ListTopicsResponse, Topic> response = managedKafkaClient.ListTopicsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Topic item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListTopicsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Topic item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Topic> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Topic item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTopicsAsync(ListTopicsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTopicsResponse, Topic> ListTopicsAsync(ListTopicsRequest request, CallSettings callSettings = null)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListTopicsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A pageable asynchronous sequence of [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ListTopicsRequest request = new ListTopicsRequest
    {
        ParentAsClusterName = ClusterName.FromProjectLocationCluster("[PROJECT]", "[LOCATION]", "[CLUSTER]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListTopicsResponse, Topic> response = managedKafkaClient.ListTopicsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Topic item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListTopicsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Topic item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Topic> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Topic item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListTopicsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListTopicsResponse, Topic> ListTopicsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists the topics in a given cluster.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent cluster whose topics are to be listed. Structured like `projects/{project}/locations/{location}/clusters/{cluster}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListTopicsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ListTopicsResponse)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A pageable asynchronous sequence of [Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic) resources.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]";
    // Make the request
    PagedAsyncEnumerable<ListTopicsResponse, Topic> response = managedKafkaClient.ListTopicsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await response.ForEachAsync((Topic item) =>
    {
        // Do something with each item
        Console.WriteLine(item);
    });
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await response.AsRawResponses().ForEachAsync((ListTopicsResponse page) =>
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Topic item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    });
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Topic> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Topic item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceCreateCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceCreateClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceDeleteCluster(string, CallSettings)
    
    
    public virtual Operation<Empty, OperationMetadata> PollOnceDeleteCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, OperationMetadata>> PollOnceDeleteClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### PollOnceUpdateCluster(string, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> PollOnceUpdateCluster(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `UpdateCluster`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceUpdateClusterAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> PollOnceUpdateClusterAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `UpdateCluster`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A task representing the result of polling the operation.  
  
### RemoveAclEntry(AclName, AclEntry, CallSettings)
    
    
    public virtual RemoveAclEntryResponse RemoveAclEntry(AclName acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to remove the acl entry from. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to remove.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    AclName acl = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    AclEntry aclEntry = new AclEntry();
    // Make the request
    RemoveAclEntryResponse response = managedKafkaClient.RemoveAclEntry(acl, aclEntry);
    

### RemoveAclEntry(RemoveAclEntryRequest, CallSettings)
    
    
    public virtual RemoveAclEntryResponse RemoveAclEntry(RemoveAclEntryRequest request, CallSettings callSettings = null)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    RemoveAclEntryRequest request = new RemoveAclEntryRequest
    {
        AclAsAclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
        AclEntry = new AclEntry(),
    };
    // Make the request
    RemoveAclEntryResponse response = managedKafkaClient.RemoveAclEntry(request);
    

### RemoveAclEntry(string, AclEntry, CallSettings)
    
    
    public virtual RemoveAclEntryResponse RemoveAclEntry(string acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to remove the acl entry from. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to remove.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    string acl = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    AclEntry aclEntry = new AclEntry();
    // Make the request
    RemoveAclEntryResponse response = managedKafkaClient.RemoveAclEntry(acl, aclEntry);
    

### RemoveAclEntryAsync(AclName, AclEntry, CallSettings)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntryAsync(AclName acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to remove the acl entry from. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to remove.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName acl = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    AclEntry aclEntry = new AclEntry();
    // Make the request
    RemoveAclEntryResponse response = await managedKafkaClient.RemoveAclEntryAsync(acl, aclEntry);
    

### RemoveAclEntryAsync(AclName, AclEntry, CancellationToken)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntryAsync(AclName acl, AclEntry aclEntry, CancellationToken cancellationToken)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[AclName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclName)`  
Required. The name of the acl to remove the acl entry from. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to remove.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    AclName acl = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]");
    AclEntry aclEntry = new AclEntry();
    // Make the request
    RemoveAclEntryResponse response = await managedKafkaClient.RemoveAclEntryAsync(acl, aclEntry);
    

### RemoveAclEntryAsync(RemoveAclEntryRequest, CallSettings)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntryAsync(RemoveAclEntryRequest request, CallSettings callSettings = null)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    RemoveAclEntryRequest request = new RemoveAclEntryRequest
    {
        AclAsAclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
        AclEntry = new AclEntry(),
    };
    // Make the request
    RemoveAclEntryResponse response = await managedKafkaClient.RemoveAclEntryAsync(request);
    

### RemoveAclEntryAsync(RemoveAclEntryRequest, CancellationToken)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntryAsync(RemoveAclEntryRequest request, CancellationToken cancellationToken)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`request` | `[RemoveAclEntryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    RemoveAclEntryRequest request = new RemoveAclEntryRequest
    {
        AclAsAclName = AclName.FromProjectLocationClusterAcl("[PROJECT]", "[LOCATION]", "[CLUSTER]", "[ACL]"),
        AclEntry = new AclEntry(),
    };
    // Make the request
    RemoveAclEntryResponse response = await managedKafkaClient.RemoveAclEntryAsync(request);
    

### RemoveAclEntryAsync(string, AclEntry, CallSettings)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntryAsync(string acl, AclEntry aclEntry, CallSettings callSettings = null)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to remove the acl entry from. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to remove.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string acl = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    AclEntry aclEntry = new AclEntry();
    // Make the request
    RemoveAclEntryResponse response = await managedKafkaClient.RemoveAclEntryAsync(acl, aclEntry);
    

### RemoveAclEntryAsync(string, AclEntry, CancellationToken)
    
    
    public virtual Task<RemoveAclEntryResponse> RemoveAclEntryAsync(string acl, AclEntry aclEntry, CancellationToken cancellationToken)

Incremental update: Removes an acl entry from an acl. Deletes the acl if its acl entries become empty (i.e. if the removed entry was the last one in the acl).

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the acl to remove the acl entry from. Structured like: `projects/{project}/locations/{location}/clusters/{cluster}/acls/{acl_id}`. The structure of `acl_id` defines the Resource Pattern (resource_type, resource_name, pattern_type) of the acl. See `Acl.name` for details.  
`aclEntry` | `[AclEntry](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.AclEntry)`  
Required. The acl entry to remove.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[RemoveAclEntryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.RemoveAclEntryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    string acl = "projects/[PROJECT]/locations/[LOCATION]/clusters/[CLUSTER]/acls/[ACL]";
    AclEntry aclEntry = new AclEntry();
    // Make the request
    RemoveAclEntryResponse response = await managedKafkaClient.RemoveAclEntryAsync(acl, aclEntry);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ManagedKafkaClient#Google_Cloud_ManagedKafka_V1_ManagedKafkaClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateAcl(Acl, FieldMask, CallSettings)
    
    
    public virtual Acl UpdateAcl(Acl acl, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. The updated acl. Its `name` and `etag` fields must be populated. `acl_entries` must not be empty in the updated acl; to remove all acl entries for an acl, use DeleteAcl.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Acl resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    Acl acl = new Acl();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Acl response = managedKafkaClient.UpdateAcl(acl, updateMask);
    

### UpdateAcl(UpdateAclRequest, CallSettings)
    
    
    public virtual Acl UpdateAcl(UpdateAclRequest request, CallSettings callSettings = null)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    UpdateAclRequest request = new UpdateAclRequest
    {
        Acl = new Acl(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Acl response = managedKafkaClient.UpdateAcl(request);
    

### UpdateAclAsync(Acl, FieldMask, CallSettings)
    
    
    public virtual Task<Acl> UpdateAclAsync(Acl acl, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. The updated acl. Its `name` and `etag` fields must be populated. `acl_entries` must not be empty in the updated acl; to remove all acl entries for an acl, use DeleteAcl.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Acl resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    Acl acl = new Acl();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Acl response = await managedKafkaClient.UpdateAclAsync(acl, updateMask);
    

### UpdateAclAsync(Acl, FieldMask, CancellationToken)
    
    
    public virtual Task<Acl> UpdateAclAsync(Acl acl, FieldMask updateMask, CancellationToken cancellationToken)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`acl` | `[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)`  
Required. The updated acl. Its `name` and `etag` fields must be populated. `acl_entries` must not be empty in the updated acl; to remove all acl entries for an acl, use DeleteAcl.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Optional. Field mask is used to specify the fields to be overwritten in the Acl resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    Acl acl = new Acl();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Acl response = await managedKafkaClient.UpdateAclAsync(acl, updateMask);
    

### UpdateAclAsync(UpdateAclRequest, CallSettings)
    
    
    public virtual Task<Acl> UpdateAclAsync(UpdateAclRequest request, CallSettings callSettings = null)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateAclRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAclRequest request = new UpdateAclRequest
    {
        Acl = new Acl(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Acl response = await managedKafkaClient.UpdateAclAsync(request);
    

### UpdateAclAsync(UpdateAclRequest, CancellationToken)
    
    
    public virtual Task<Acl> UpdateAclAsync(UpdateAclRequest request, CancellationToken cancellationToken)

Updates the properties of a single acl.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateAclRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateAclRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Acl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Acl)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateAclRequest request = new UpdateAclRequest
    {
        Acl = new Acl(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Acl response = await managedKafkaClient.UpdateAclAsync(request);
    

### UpdateCluster(Cluster, FieldMask, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> UpdateCluster(Cluster cluster, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. The cluster to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    Cluster cluster = new Cluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Cluster, OperationMetadata> response = managedKafkaClient.UpdateCluster(cluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceUpdateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateCluster(UpdateClusterRequest, CallSettings)
    
    
    public virtual Operation<Cluster, OperationMetadata> UpdateCluster(UpdateClusterRequest request, CallSettings callSettings = null)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    UpdateClusterRequest request = new UpdateClusterRequest
    {
        UpdateMask = new FieldMask(),
        Cluster = new Cluster(),
        RequestId = "",
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = managedKafkaClient.UpdateCluster(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = managedKafkaClient.PollOnceUpdateCluster(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(Cluster, FieldMask, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(Cluster cluster, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. The cluster to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    Cluster cluster = new Cluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.UpdateClusterAsync(cluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(Cluster, FieldMask, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(Cluster cluster, FieldMask updateMask, CancellationToken cancellationToken)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`cluster` | `[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)`  
Required. The cluster to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the cluster resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    Cluster cluster = new Cluster();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.UpdateClusterAsync(cluster, updateMask);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(UpdateClusterRequest, CallSettings)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(UpdateClusterRequest request, CallSettings callSettings = null)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateClusterRequest request = new UpdateClusterRequest
    {
        UpdateMask = new FieldMask(),
        Cluster = new Cluster(),
        RequestId = "",
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.UpdateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateClusterAsync(UpdateClusterRequest, CancellationToken)
    
    
    public virtual Task<Operation<Cluster, OperationMetadata>> UpdateClusterAsync(UpdateClusterRequest request, CancellationToken cancellationToken)

Updates the properties of a single cluster.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateClusterRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateClusterRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Cluster](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Cluster)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateClusterRequest request = new UpdateClusterRequest
    {
        UpdateMask = new FieldMask(),
        Cluster = new Cluster(),
        RequestId = "",
    };
    // Make the request
    Operation<Cluster, OperationMetadata> response = await managedKafkaClient.UpdateClusterAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Cluster, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Cluster result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Cluster, OperationMetadata> retrievedResponse = await managedKafkaClient.PollOnceUpdateClusterAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Cluster retrievedResult = retrievedResponse.Result;
    }
    

### UpdateConsumerGroup(ConsumerGroup, FieldMask, CallSettings)
    
    
    public virtual ConsumerGroup UpdateConsumerGroup(ConsumerGroup consumerGroup, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`consumerGroup` | `[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)`  
Required. The consumer group to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the ConsumerGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    ConsumerGroup consumerGroup = new ConsumerGroup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    ConsumerGroup response = managedKafkaClient.UpdateConsumerGroup(consumerGroup, updateMask);
    

### UpdateConsumerGroup(UpdateConsumerGroupRequest, CallSettings)
    
    
    public virtual ConsumerGroup UpdateConsumerGroup(UpdateConsumerGroupRequest request, CallSettings callSettings = null)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    UpdateConsumerGroupRequest request = new UpdateConsumerGroupRequest
    {
        UpdateMask = new FieldMask(),
        ConsumerGroup = new ConsumerGroup(),
    };
    // Make the request
    ConsumerGroup response = managedKafkaClient.UpdateConsumerGroup(request);
    

### UpdateConsumerGroupAsync(ConsumerGroup, FieldMask, CallSettings)
    
    
    public virtual Task<ConsumerGroup> UpdateConsumerGroupAsync(ConsumerGroup consumerGroup, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`consumerGroup` | `[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)`  
Required. The consumer group to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the ConsumerGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ConsumerGroup consumerGroup = new ConsumerGroup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    ConsumerGroup response = await managedKafkaClient.UpdateConsumerGroupAsync(consumerGroup, updateMask);
    

### UpdateConsumerGroupAsync(ConsumerGroup, FieldMask, CancellationToken)
    
    
    public virtual Task<ConsumerGroup> UpdateConsumerGroupAsync(ConsumerGroup consumerGroup, FieldMask updateMask, CancellationToken cancellationToken)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`consumerGroup` | `[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)`  
Required. The consumer group to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the ConsumerGroup resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    ConsumerGroup consumerGroup = new ConsumerGroup();
    FieldMask updateMask = new FieldMask();
    // Make the request
    ConsumerGroup response = await managedKafkaClient.UpdateConsumerGroupAsync(consumerGroup, updateMask);
    

### UpdateConsumerGroupAsync(UpdateConsumerGroupRequest, CallSettings)
    
    
    public virtual Task<ConsumerGroup> UpdateConsumerGroupAsync(UpdateConsumerGroupRequest request, CallSettings callSettings = null)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConsumerGroupRequest request = new UpdateConsumerGroupRequest
    {
        UpdateMask = new FieldMask(),
        ConsumerGroup = new ConsumerGroup(),
    };
    // Make the request
    ConsumerGroup response = await managedKafkaClient.UpdateConsumerGroupAsync(request);
    

### UpdateConsumerGroupAsync(UpdateConsumerGroupRequest, CancellationToken)
    
    
    public virtual Task<ConsumerGroup> UpdateConsumerGroupAsync(UpdateConsumerGroupRequest request, CancellationToken cancellationToken)

Updates the properties of a single consumer group.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateConsumerGroupRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateConsumerGroupRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConsumerGroup](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.ConsumerGroup)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateConsumerGroupRequest request = new UpdateConsumerGroupRequest
    {
        UpdateMask = new FieldMask(),
        ConsumerGroup = new ConsumerGroup(),
    };
    // Make the request
    ConsumerGroup response = await managedKafkaClient.UpdateConsumerGroupAsync(request);
    

### UpdateTopic(Topic, FieldMask, CallSettings)
    
    
    public virtual Topic UpdateTopic(Topic topic, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. The topic to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Topic resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    Topic topic = new Topic();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Topic response = managedKafkaClient.UpdateTopic(topic, updateMask);
    

### UpdateTopic(UpdateTopicRequest, CallSettings)
    
    
    public virtual Topic UpdateTopic(UpdateTopicRequest request, CallSettings callSettings = null)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | The RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = ManagedKafkaClient.Create();
    // Initialize request argument(s)
    UpdateTopicRequest request = new UpdateTopicRequest
    {
        UpdateMask = new FieldMask(),
        Topic = new Topic(),
    };
    // Make the request
    Topic response = managedKafkaClient.UpdateTopic(request);
    

### UpdateTopicAsync(Topic, FieldMask, CallSettings)
    
    
    public virtual Task<Topic> UpdateTopicAsync(Topic topic, FieldMask updateMask, CallSettings callSettings = null)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. The topic to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Topic resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    Topic topic = new Topic();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Topic response = await managedKafkaClient.UpdateTopicAsync(topic, updateMask);
    

### UpdateTopicAsync(Topic, FieldMask, CancellationToken)
    
    
    public virtual Task<Topic> UpdateTopicAsync(Topic topic, FieldMask updateMask, CancellationToken cancellationToken)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`topic` | `[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)`  
Required. The topic to update. Its `name` field must be populated.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. Field mask is used to specify the fields to be overwritten in the Topic resource by the update. The fields specified in the update_mask are relative to the resource, not the full request. A field will be overwritten if it is in the mask. The mask is required and a value of * will update all fields.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    Topic topic = new Topic();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Topic response = await managedKafkaClient.UpdateTopicAsync(topic, updateMask);
    

### UpdateTopicAsync(UpdateTopicRequest, CallSettings)
    
    
    public virtual Task<Topic> UpdateTopicAsync(UpdateTopicRequest request, CallSettings callSettings = null)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateTopicRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateTopicRequest request = new UpdateTopicRequest
    {
        UpdateMask = new FieldMask(),
        Topic = new Topic(),
    };
    // Make the request
    Topic response = await managedKafkaClient.UpdateTopicAsync(request);
    

### UpdateTopicAsync(UpdateTopicRequest, CancellationToken)
    
    
    public virtual Task<Topic> UpdateTopicAsync(UpdateTopicRequest request, CancellationToken cancellationToken)

Updates the properties of a single topic.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateTopicRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.UpdateTopicRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Topic](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ManagedKafka.V1/latest/Google.Cloud.ManagedKafka.V1.Topic)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ManagedKafkaClient managedKafkaClient = await ManagedKafkaClient.CreateAsync();
    // Initialize request argument(s)
    UpdateTopicRequest request = new UpdateTopicRequest
    {
        UpdateMask = new FieldMask(),
        Topic = new Topic(),
    };
    // Make the request
    Topic response = await managedKafkaClient.UpdateTopicAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
