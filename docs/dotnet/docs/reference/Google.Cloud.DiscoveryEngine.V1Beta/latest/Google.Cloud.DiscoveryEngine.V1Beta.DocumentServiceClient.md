---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient
title: Discovery Engine v1beta API - Class DocumentServiceClient (1.0.0-beta25) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:24:45.714201+00:00
---

# Discovery Engine v1beta API - Class DocumentServiceClient (1.0.0-beta25)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1beta API - Class DocumentServiceClient (1.0.0-beta25) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta25 (latest)  1.0.0-beta24 
    
    
    public abstract class DocumentServiceClient

Reference documentation and code samples for the Discovery Engine v1beta API class DocumentServiceClient.

DocumentService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DocumentServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[DocumentServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClientImpl)

## Namespace

[Google.Cloud.DiscoveryEngine.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta)

## Assembly

Google.Cloud.DiscoveryEngine.V1Beta.dll

## Remarks

Service for ingesting [Document][google.cloud.discoveryengine.v1beta.Document] information of the customer's website.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the DocumentService service, which is a host of "discoveryengine.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default DocumentService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default DocumentService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/discoveryengine.readwrite>
  * <https://www.googleapis.com/auth/discoveryengine.serving.readwrite>



### GrpcClient
    
    
    public virtual DocumentService.DocumentServiceClient GrpcClient { get; }

The underlying gRPC DocumentService client

**Property Value**  
---  
**Type** | **Description**  
`[DocumentService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentService)[DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentService.DocumentServiceClient)` |   
  
### ImportDocumentsOperationsClient
    
    
    public virtual OperationsClient ImportDocumentsOperationsClient { get; }

The long-running operations client for `ImportDocuments`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### LocationsClient
    
    
    public virtual LocationsClient LocationsClient { get; }

The [LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html) associated with this client.

**Property Value**  
---  
**Type** | **Description**  
`[LocationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Location/latest/Google.Cloud.Location.LocationsClient.html)` |   
  
### PurgeDocumentsOperationsClient
    
    
    public virtual OperationsClient PurgeDocumentsOperationsClient { get; }

The long-running operations client for `PurgeDocuments`.

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
  
## Methods 

### BatchGetDocumentsMetadata(BatchGetDocumentsMetadataRequest, CallSettings)
    
    
    public virtual BatchGetDocumentsMetadataResponse BatchGetDocumentsMetadata(BatchGetDocumentsMetadataRequest request, CallSettings callSettings = null)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    BatchGetDocumentsMetadataRequest request = new BatchGetDocumentsMetadataRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Matcher = new BatchGetDocumentsMetadataRequest.Types.Matcher(),
    };
    // Make the request
    BatchGetDocumentsMetadataResponse response = documentServiceClient.BatchGetDocumentsMetadata(request);
    

### BatchGetDocumentsMetadata(BranchName, CallSettings)
    
    
    public virtual BatchGetDocumentsMetadataResponse BatchGetDocumentsMetadata(BranchName parent, CallSettings callSettings = null)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    // Make the request
    BatchGetDocumentsMetadataResponse response = documentServiceClient.BatchGetDocumentsMetadata(parent);
    

### BatchGetDocumentsMetadata(string, CallSettings)
    
    
    public virtual BatchGetDocumentsMetadataResponse BatchGetDocumentsMetadata(string parent, CallSettings callSettings = null)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    // Make the request
    BatchGetDocumentsMetadataResponse response = documentServiceClient.BatchGetDocumentsMetadata(parent);
    

### BatchGetDocumentsMetadataAsync(BatchGetDocumentsMetadataRequest, CallSettings)
    
    
    public virtual Task<BatchGetDocumentsMetadataResponse> BatchGetDocumentsMetadataAsync(BatchGetDocumentsMetadataRequest request, CallSettings callSettings = null)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchGetDocumentsMetadataRequest request = new BatchGetDocumentsMetadataRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Matcher = new BatchGetDocumentsMetadataRequest.Types.Matcher(),
    };
    // Make the request
    BatchGetDocumentsMetadataResponse response = await documentServiceClient.BatchGetDocumentsMetadataAsync(request);
    

### BatchGetDocumentsMetadataAsync(BatchGetDocumentsMetadataRequest, CancellationToken)
    
    
    public virtual Task<BatchGetDocumentsMetadataResponse> BatchGetDocumentsMetadataAsync(BatchGetDocumentsMetadataRequest request, CancellationToken cancellationToken)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchGetDocumentsMetadataRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BatchGetDocumentsMetadataRequest request = new BatchGetDocumentsMetadataRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Matcher = new BatchGetDocumentsMetadataRequest.Types.Matcher(),
    };
    // Make the request
    BatchGetDocumentsMetadataResponse response = await documentServiceClient.BatchGetDocumentsMetadataAsync(request);
    

### BatchGetDocumentsMetadataAsync(BranchName, CallSettings)
    
    
    public virtual Task<BatchGetDocumentsMetadataResponse> BatchGetDocumentsMetadataAsync(BranchName parent, CallSettings callSettings = null)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    // Make the request
    BatchGetDocumentsMetadataResponse response = await documentServiceClient.BatchGetDocumentsMetadataAsync(parent);
    

### BatchGetDocumentsMetadataAsync(BranchName, CancellationToken)
    
    
    public virtual Task<BatchGetDocumentsMetadataResponse> BatchGetDocumentsMetadataAsync(BranchName parent, CancellationToken cancellationToken)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    // Make the request
    BatchGetDocumentsMetadataResponse response = await documentServiceClient.BatchGetDocumentsMetadataAsync(parent);
    

### BatchGetDocumentsMetadataAsync(string, CallSettings)
    
    
    public virtual Task<BatchGetDocumentsMetadataResponse> BatchGetDocumentsMetadataAsync(string parent, CallSettings callSettings = null)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    // Make the request
    BatchGetDocumentsMetadataResponse response = await documentServiceClient.BatchGetDocumentsMetadataAsync(parent);
    

### BatchGetDocumentsMetadataAsync(string, CancellationToken)
    
    
    public virtual Task<BatchGetDocumentsMetadataResponse> BatchGetDocumentsMetadataAsync(string parent, CancellationToken cancellationToken)

Gets index freshness metadata for [Document][google.cloud.discoveryengine.v1beta.Document]s. Supported for website search only.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchGetDocumentsMetadataResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BatchGetDocumentsMetadataResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    // Make the request
    BatchGetDocumentsMetadataResponse response = await documentServiceClient.BatchGetDocumentsMetadataAsync(parent);
    

### Create()
    
    
    public static DocumentServiceClient Create()

Synchronously creates a [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DocumentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient)` | The created [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<DocumentServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [DocumentServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient)` | The task representing the created [DocumentServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient).  
  
### CreateDocument(BranchName, Document, string, CallSettings)
    
    
    public virtual Document CreateDocument(BranchName parent, Document document, string documentId, CallSettings callSettings = null)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The [Document][google.cloud.discoveryengine.v1beta.Document] to create.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Document][google.cloud.discoveryengine.v1beta.Document], which becomes the final component of the [Document.name][google.cloud.discoveryengine.v1beta.Document.name]. If the caller does not have permission to create the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all [Document][google.cloud.discoveryengine.v1beta.Document]s with the same [parent][google.cloud.discoveryengine.v1beta.CreateDocumentRequest.parent]. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    Document document = new Document();
    string documentId = "";
    // Make the request
    Document response = documentServiceClient.CreateDocument(parent, document, documentId);
    

### CreateDocument(CreateDocumentRequest, CallSettings)
    
    
    public virtual Document CreateDocument(CreateDocumentRequest request, CallSettings callSettings = null)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    CreateDocumentRequest request = new CreateDocumentRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Document = new Document(),
        DocumentId = "",
    };
    // Make the request
    Document response = documentServiceClient.CreateDocument(request);
    

### CreateDocument(string, Document, string, CallSettings)
    
    
    public virtual Document CreateDocument(string parent, Document document, string documentId, CallSettings callSettings = null)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The [Document][google.cloud.discoveryengine.v1beta.Document] to create.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Document][google.cloud.discoveryengine.v1beta.Document], which becomes the final component of the [Document.name][google.cloud.discoveryengine.v1beta.Document.name]. If the caller does not have permission to create the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all [Document][google.cloud.discoveryengine.v1beta.Document]s with the same [parent][google.cloud.discoveryengine.v1beta.CreateDocumentRequest.parent]. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    Document document = new Document();
    string documentId = "";
    // Make the request
    Document response = documentServiceClient.CreateDocument(parent, document, documentId);
    

### CreateDocumentAsync(BranchName, Document, string, CallSettings)
    
    
    public virtual Task<Document> CreateDocumentAsync(BranchName parent, Document document, string documentId, CallSettings callSettings = null)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The [Document][google.cloud.discoveryengine.v1beta.Document] to create.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Document][google.cloud.discoveryengine.v1beta.Document], which becomes the final component of the [Document.name][google.cloud.discoveryengine.v1beta.Document.name]. If the caller does not have permission to create the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all [Document][google.cloud.discoveryengine.v1beta.Document]s with the same [parent][google.cloud.discoveryengine.v1beta.CreateDocumentRequest.parent]. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    Document document = new Document();
    string documentId = "";
    // Make the request
    Document response = await documentServiceClient.CreateDocumentAsync(parent, document, documentId);
    

### CreateDocumentAsync(BranchName, Document, string, CancellationToken)
    
    
    public virtual Task<Document> CreateDocumentAsync(BranchName parent, Document document, string documentId, CancellationToken cancellationToken)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The [Document][google.cloud.discoveryengine.v1beta.Document] to create.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Document][google.cloud.discoveryengine.v1beta.Document], which becomes the final component of the [Document.name][google.cloud.discoveryengine.v1beta.Document.name]. If the caller does not have permission to create the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all [Document][google.cloud.discoveryengine.v1beta.Document]s with the same [parent][google.cloud.discoveryengine.v1beta.CreateDocumentRequest.parent]. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    Document document = new Document();
    string documentId = "";
    // Make the request
    Document response = await documentServiceClient.CreateDocumentAsync(parent, document, documentId);
    

### CreateDocumentAsync(CreateDocumentRequest, CallSettings)
    
    
    public virtual Task<Document> CreateDocumentAsync(CreateDocumentRequest request, CallSettings callSettings = null)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateDocumentRequest request = new CreateDocumentRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Document = new Document(),
        DocumentId = "",
    };
    // Make the request
    Document response = await documentServiceClient.CreateDocumentAsync(request);
    

### CreateDocumentAsync(CreateDocumentRequest, CancellationToken)
    
    
    public virtual Task<Document> CreateDocumentAsync(CreateDocumentRequest request, CancellationToken cancellationToken)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.CreateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateDocumentRequest request = new CreateDocumentRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Document = new Document(),
        DocumentId = "",
    };
    // Make the request
    Document response = await documentServiceClient.CreateDocumentAsync(request);
    

### CreateDocumentAsync(string, Document, string, CallSettings)
    
    
    public virtual Task<Document> CreateDocumentAsync(string parent, Document document, string documentId, CallSettings callSettings = null)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The [Document][google.cloud.discoveryengine.v1beta.Document] to create.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Document][google.cloud.discoveryengine.v1beta.Document], which becomes the final component of the [Document.name][google.cloud.discoveryengine.v1beta.Document.name]. If the caller does not have permission to create the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all [Document][google.cloud.discoveryengine.v1beta.Document]s with the same [parent][google.cloud.discoveryengine.v1beta.CreateDocumentRequest.parent]. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    Document document = new Document();
    string documentId = "";
    // Make the request
    Document response = await documentServiceClient.CreateDocumentAsync(parent, document, documentId);
    

### CreateDocumentAsync(string, Document, string, CancellationToken)
    
    
    public virtual Task<Document> CreateDocumentAsync(string parent, Document document, string documentId, CancellationToken cancellationToken)

Creates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`.  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The [Document][google.cloud.discoveryengine.v1beta.Document] to create.  
`documentId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for the [Document][google.cloud.discoveryengine.v1beta.Document], which becomes the final component of the [Document.name][google.cloud.discoveryengine.v1beta.Document.name]. If the caller does not have permission to create the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. This field must be unique among all [Document][google.cloud.discoveryengine.v1beta.Document]s with the same [parent][google.cloud.discoveryengine.v1beta.CreateDocumentRequest.parent]. Otherwise, an `ALREADY_EXISTS` error is returned. This field must conform to [RFC-1034](https://tools.ietf.org/html/rfc1034) standard with a length limit of 128 characters. Otherwise, an `INVALID_ARGUMENT` error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    Document document = new Document();
    string documentId = "";
    // Make the request
    Document response = await documentServiceClient.CreateDocumentAsync(parent, document, documentId);
    

### DeleteDocument(DeleteDocumentRequest, CallSettings)
    
    
    public virtual void DeleteDocument(DeleteDocumentRequest request, CallSettings callSettings = null)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    DeleteDocumentRequest request = new DeleteDocumentRequest
    {
        DocumentName = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]"),
    };
    // Make the request
    documentServiceClient.DeleteDocument(request);
    

### DeleteDocument(DocumentName, CallSettings)
    
    
    public virtual void DeleteDocument(DocumentName name, CallSettings callSettings = null)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentName)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to delete does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    DocumentName name = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
    // Make the request
    documentServiceClient.DeleteDocument(name);
    

### DeleteDocument(string, CallSettings)
    
    
    public virtual void DeleteDocument(string name, CallSettings callSettings = null)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to delete does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]/documents/[DOCUMENT]";
    // Make the request
    documentServiceClient.DeleteDocument(name);
    

### DeleteDocumentAsync(DeleteDocumentRequest, CallSettings)
    
    
    public virtual Task DeleteDocumentAsync(DeleteDocumentRequest request, CallSettings callSettings = null)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDocumentRequest request = new DeleteDocumentRequest
    {
        DocumentName = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]"),
    };
    // Make the request
    await documentServiceClient.DeleteDocumentAsync(request);
    

### DeleteDocumentAsync(DeleteDocumentRequest, CancellationToken)
    
    
    public virtual Task DeleteDocumentAsync(DeleteDocumentRequest request, CancellationToken cancellationToken)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DeleteDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteDocumentRequest request = new DeleteDocumentRequest
    {
        DocumentName = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]"),
    };
    // Make the request
    await documentServiceClient.DeleteDocumentAsync(request);
    

### DeleteDocumentAsync(DocumentName, CallSettings)
    
    
    public virtual Task DeleteDocumentAsync(DocumentName name, CallSettings callSettings = null)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentName)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to delete does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DocumentName name = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
    // Make the request
    await documentServiceClient.DeleteDocumentAsync(name);
    

### DeleteDocumentAsync(DocumentName, CancellationToken)
    
    
    public virtual Task DeleteDocumentAsync(DocumentName name, CancellationToken cancellationToken)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentName)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to delete does not exist, a `NOT_FOUND` error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DocumentName name = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
    // Make the request
    await documentServiceClient.DeleteDocumentAsync(name);
    

### DeleteDocumentAsync(string, CallSettings)
    
    
    public virtual Task DeleteDocumentAsync(string name, CallSettings callSettings = null)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to delete does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]/documents/[DOCUMENT]";
    // Make the request
    await documentServiceClient.DeleteDocumentAsync(name);
    

### DeleteDocumentAsync(string, CancellationToken)
    
    
    public virtual Task DeleteDocumentAsync(string name, CancellationToken cancellationToken)

Deletes a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to delete the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to delete does not exist, a `NOT_FOUND` error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]/documents/[DOCUMENT]";
    // Make the request
    await documentServiceClient.DeleteDocumentAsync(name);
    

### GetDocument(DocumentName, CallSettings)
    
    
    public virtual Document GetDocument(DocumentName name, CallSettings callSettings = null)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentName)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested [Document][google.cloud.discoveryengine.v1beta.Document] does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    DocumentName name = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
    // Make the request
    Document response = documentServiceClient.GetDocument(name);
    

### GetDocument(GetDocumentRequest, CallSettings)
    
    
    public virtual Document GetDocument(GetDocumentRequest request, CallSettings callSettings = null)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    GetDocumentRequest request = new GetDocumentRequest
    {
        DocumentName = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]"),
    };
    // Make the request
    Document response = documentServiceClient.GetDocument(request);
    

### GetDocument(string, CallSettings)
    
    
    public virtual Document GetDocument(string name, CallSettings callSettings = null)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested [Document][google.cloud.discoveryengine.v1beta.Document] does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]/documents/[DOCUMENT]";
    // Make the request
    Document response = documentServiceClient.GetDocument(name);
    

### GetDocumentAsync(DocumentName, CallSettings)
    
    
    public virtual Task<Document> GetDocumentAsync(DocumentName name, CallSettings callSettings = null)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentName)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested [Document][google.cloud.discoveryengine.v1beta.Document] does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DocumentName name = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
    // Make the request
    Document response = await documentServiceClient.GetDocumentAsync(name);
    

### GetDocumentAsync(DocumentName, CancellationToken)
    
    
    public virtual Task<Document> GetDocumentAsync(DocumentName name, CancellationToken cancellationToken)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[DocumentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentName)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested [Document][google.cloud.discoveryengine.v1beta.Document] does not exist, a `NOT_FOUND` error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    DocumentName name = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]");
    // Make the request
    Document response = await documentServiceClient.GetDocumentAsync(name);
    

### GetDocumentAsync(GetDocumentRequest, CallSettings)
    
    
    public virtual Task<Document> GetDocumentAsync(GetDocumentRequest request, CallSettings callSettings = null)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDocumentRequest request = new GetDocumentRequest
    {
        DocumentName = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]"),
    };
    // Make the request
    Document response = await documentServiceClient.GetDocumentAsync(request);
    

### GetDocumentAsync(GetDocumentRequest, CancellationToken)
    
    
    public virtual Task<Document> GetDocumentAsync(GetDocumentRequest request, CancellationToken cancellationToken)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.GetDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetDocumentRequest request = new GetDocumentRequest
    {
        DocumentName = DocumentName.FromProjectLocationDataStoreBranchDocument("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]", "[DOCUMENT]"),
    };
    // Make the request
    Document response = await documentServiceClient.GetDocumentAsync(request);
    

### GetDocumentAsync(string, CallSettings)
    
    
    public virtual Task<Document> GetDocumentAsync(string name, CallSettings callSettings = null)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested [Document][google.cloud.discoveryengine.v1beta.Document] does not exist, a `NOT_FOUND` error is returned.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]/documents/[DOCUMENT]";
    // Make the request
    Document response = await documentServiceClient.GetDocumentAsync(name);
    

### GetDocumentAsync(string, CancellationToken)
    
    
    public virtual Task<Document> GetDocumentAsync(string name, CancellationToken cancellationToken)

Gets a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Full resource name of [Document][google.cloud.discoveryengine.v1beta.Document], such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}/documents/{document}`. If the caller does not have permission to access the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the requested [Document][google.cloud.discoveryengine.v1beta.Document] does not exist, a `NOT_FOUND` error is returned.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]/documents/[DOCUMENT]";
    // Make the request
    Document response = await documentServiceClient.GetDocumentAsync(name);
    

### ImportDocuments(ImportDocumentsRequest, CallSettings)
    
    
    public virtual Operation<ImportDocumentsResponse, ImportDocumentsMetadata> ImportDocuments(ImportDocumentsRequest request, CallSettings callSettings = null)

Bulk import of multiple [Document][google.cloud.discoveryengine.v1beta.Document]s. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the [Document][google.cloud.discoveryengine.v1beta.Document]s to be successfully updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsResponse)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    ImportDocumentsRequest request = new ImportDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
        ErrorConfig = new ImportErrorConfig(),
        ReconciliationMode = ImportDocumentsRequest.Types.ReconciliationMode.Unspecified,
        UpdateMask = new FieldMask(),
        AutoGenerateIds = false,
        IdField = "",
        ForceRefreshContent = false,
    };
    // Make the request
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = documentServiceClient.ImportDocuments(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    ImportDocumentsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = documentServiceClient.PollOnceImportDocuments(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDocumentsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDocumentsAsync(ImportDocumentsRequest, CallSettings)
    
    
    public virtual Task<Operation<ImportDocumentsResponse, ImportDocumentsMetadata>> ImportDocumentsAsync(ImportDocumentsRequest request, CallSettings callSettings = null)

Bulk import of multiple [Document][google.cloud.discoveryengine.v1beta.Document]s. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the [Document][google.cloud.discoveryengine.v1beta.Document]s to be successfully updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsResponse)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ImportDocumentsRequest request = new ImportDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
        ErrorConfig = new ImportErrorConfig(),
        ReconciliationMode = ImportDocumentsRequest.Types.ReconciliationMode.Unspecified,
        UpdateMask = new FieldMask(),
        AutoGenerateIds = false,
        IdField = "",
        ForceRefreshContent = false,
    };
    // Make the request
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = await documentServiceClient.ImportDocumentsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDocumentsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = await documentServiceClient.PollOnceImportDocumentsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDocumentsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ImportDocumentsAsync(ImportDocumentsRequest, CancellationToken)
    
    
    public virtual Task<Operation<ImportDocumentsResponse, ImportDocumentsMetadata>> ImportDocumentsAsync(ImportDocumentsRequest request, CancellationToken cancellationToken)

Bulk import of multiple [Document][google.cloud.discoveryengine.v1beta.Document]s. Request processing may be synchronous. Non-existing items are created.

Note: It is possible for a subset of the [Document][google.cloud.discoveryengine.v1beta.Document]s to be successfully updated.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ImportDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsResponse)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ImportDocumentsRequest request = new ImportDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        InlineSource = new ImportDocumentsRequest.Types.InlineSource(),
        ErrorConfig = new ImportErrorConfig(),
        ReconciliationMode = ImportDocumentsRequest.Types.ReconciliationMode.Unspecified,
        UpdateMask = new FieldMask(),
        AutoGenerateIds = false,
        IdField = "",
        ForceRefreshContent = false,
    };
    // Make the request
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> response = await documentServiceClient.ImportDocumentsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    ImportDocumentsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<ImportDocumentsResponse, ImportDocumentsMetadata> retrievedResponse = await documentServiceClient.PollOnceImportDocumentsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        ImportDocumentsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ListDocuments(BranchName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDocumentsResponse, Document> ListDocuments(BranchName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets a list of [Document][google.cloud.discoveryengine.v1beta.Document]s.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch. If the caller does not have permission to list [Document][google.cloud.discoveryengine.v1beta.Document]s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A pageable sequence of [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document) resources.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    // Make the request
    PagedEnumerable<ListDocumentsResponse, Document> response = documentServiceClient.ListDocuments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Document item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDocumentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Document item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Document> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Document item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDocuments(ListDocumentsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListDocumentsResponse, Document> ListDocuments(ListDocumentsRequest request, CallSettings callSettings = null)

Gets a list of [Document][google.cloud.discoveryengine.v1beta.Document]s.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A pageable sequence of [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document) resources.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    ListDocumentsRequest request = new ListDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
    };
    // Make the request
    PagedEnumerable<ListDocumentsResponse, Document> response = documentServiceClient.ListDocuments(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Document item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDocumentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Document item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Document> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Document item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDocuments(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListDocumentsResponse, Document> ListDocuments(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets a list of [Document][google.cloud.discoveryengine.v1beta.Document]s.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch. If the caller does not have permission to list [Document][google.cloud.discoveryengine.v1beta.Document]s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A pageable sequence of [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document) resources.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    // Make the request
    PagedEnumerable<ListDocumentsResponse, Document> response = documentServiceClient.ListDocuments(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Document item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListDocumentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Document item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Document> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Document item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDocumentsAsync(BranchName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDocumentsResponse, Document> ListDocumentsAsync(BranchName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets a list of [Document][google.cloud.discoveryengine.v1beta.Document]s.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[BranchName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.BranchName)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch. If the caller does not have permission to list [Document][google.cloud.discoveryengine.v1beta.Document]s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A pageable asynchronous sequence of [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document) resources.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    BranchName parent = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]");
    // Make the request
    PagedAsyncEnumerable<ListDocumentsResponse, Document> response = documentServiceClient.ListDocumentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Document item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDocumentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Document item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Document> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Document item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDocumentsAsync(ListDocumentsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDocumentsResponse, Document> ListDocumentsAsync(ListDocumentsRequest request, CallSettings callSettings = null)

Gets a list of [Document][google.cloud.discoveryengine.v1beta.Document]s.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A pageable asynchronous sequence of [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document) resources.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListDocumentsRequest request = new ListDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListDocumentsResponse, Document> response = documentServiceClient.ListDocumentsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Document item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDocumentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Document item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Document> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Document item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListDocumentsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListDocumentsResponse, Document> ListDocumentsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Gets a list of [Document][google.cloud.discoveryengine.v1beta.Document]s.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent branch resource name, such as `projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/branches/{branch}`. Use `default_branch` as the branch ID, to list documents under the default branch. If the caller does not have permission to list [Document][google.cloud.discoveryengine.v1beta.Document]s under this branch, regardless of whether or not this branch exists, a `PERMISSION_DENIED` error is returned.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ListDocumentsResponse)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A pageable asynchronous sequence of [Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document) resources.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/dataStores/[DATA_STORE]/branches/[BRANCH]";
    // Make the request
    PagedAsyncEnumerable<ListDocumentsResponse, Document> response = documentServiceClient.ListDocumentsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Document item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListDocumentsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Document item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Document> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Document item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceImportDocuments(string, CallSettings)
    
    
    public virtual Operation<ImportDocumentsResponse, ImportDocumentsMetadata> PollOnceImportDocuments(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `ImportDocuments`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsResponse)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsMetadata)` | The result of polling the operation.  
  
### PollOnceImportDocumentsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<ImportDocumentsResponse, ImportDocumentsMetadata>> PollOnceImportDocumentsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `ImportDocuments`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[ImportDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsResponse)[ImportDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.ImportDocumentsMetadata)` | A task representing the result of polling the operation.  
  
### PollOncePurgeDocuments(string, CallSettings)
    
    
    public virtual Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> PollOncePurgeDocuments(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `PurgeDocuments`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsResponse)[PurgeDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsMetadata)` | The result of polling the operation.  
  
### PollOncePurgeDocumentsAsync(string, CallSettings)
    
    
    public virtual Task<Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata>> PollOncePurgeDocumentsAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `PurgeDocuments`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsResponse)[PurgeDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsMetadata)` | A task representing the result of polling the operation.  
  
### PurgeDocuments(PurgeDocumentsRequest, CallSettings)
    
    
    public virtual Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> PurgeDocuments(PurgeDocumentsRequest request, CallSettings callSettings = null)

Permanently deletes all selected [Document][google.cloud.discoveryengine.v1beta.Document]s in a branch.

This process is asynchronous. Depending on the number of [Document][google.cloud.discoveryengine.v1beta.Document]s to be deleted, this operation can take hours to complete. Before the delete operation completes, some [Document][google.cloud.discoveryengine.v1beta.Document]s might still be returned by [DocumentService.GetDocument][google.cloud.discoveryengine.v1beta.DocumentService.GetDocument] or [DocumentService.ListDocuments][google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments].

To get a list of the [Document][google.cloud.discoveryengine.v1beta.Document]s to be deleted, set [PurgeDocumentsRequest.force][google.cloud.discoveryengine.v1beta.PurgeDocumentsRequest.force] to false.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsResponse)[PurgeDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    PurgeDocumentsRequest request = new PurgeDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Filter = "",
        Force = false,
        GcsSource = new GcsSource(),
        ErrorConfig = new PurgeErrorConfig(),
    };
    // Make the request
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> response = documentServiceClient.PurgeDocuments(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    PurgeDocumentsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> retrievedResponse = documentServiceClient.PollOncePurgeDocuments(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PurgeDocumentsResponse retrievedResult = retrievedResponse.Result;
    }
    

### PurgeDocumentsAsync(PurgeDocumentsRequest, CallSettings)
    
    
    public virtual Task<Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata>> PurgeDocumentsAsync(PurgeDocumentsRequest request, CallSettings callSettings = null)

Permanently deletes all selected [Document][google.cloud.discoveryengine.v1beta.Document]s in a branch.

This process is asynchronous. Depending on the number of [Document][google.cloud.discoveryengine.v1beta.Document]s to be deleted, this operation can take hours to complete. Before the delete operation completes, some [Document][google.cloud.discoveryengine.v1beta.Document]s might still be returned by [DocumentService.GetDocument][google.cloud.discoveryengine.v1beta.DocumentService.GetDocument] or [DocumentService.ListDocuments][google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments].

To get a list of the [Document][google.cloud.discoveryengine.v1beta.Document]s to be deleted, set [PurgeDocumentsRequest.force][google.cloud.discoveryengine.v1beta.PurgeDocumentsRequest.force] to false.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsResponse)[PurgeDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    PurgeDocumentsRequest request = new PurgeDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Filter = "",
        Force = false,
        GcsSource = new GcsSource(),
        ErrorConfig = new PurgeErrorConfig(),
    };
    // Make the request
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> response = await documentServiceClient.PurgeDocumentsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PurgeDocumentsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> retrievedResponse = await documentServiceClient.PollOncePurgeDocumentsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PurgeDocumentsResponse retrievedResult = retrievedResponse.Result;
    }
    

### PurgeDocumentsAsync(PurgeDocumentsRequest, CancellationToken)
    
    
    public virtual Task<Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata>> PurgeDocumentsAsync(PurgeDocumentsRequest request, CancellationToken cancellationToken)

Permanently deletes all selected [Document][google.cloud.discoveryengine.v1beta.Document]s in a branch.

This process is asynchronous. Depending on the number of [Document][google.cloud.discoveryengine.v1beta.Document]s to be deleted, this operation can take hours to complete. Before the delete operation completes, some [Document][google.cloud.discoveryengine.v1beta.Document]s might still be returned by [DocumentService.GetDocument][google.cloud.discoveryengine.v1beta.DocumentService.GetDocument] or [DocumentService.ListDocuments][google.cloud.discoveryengine.v1beta.DocumentService.ListDocuments].

To get a list of the [Document][google.cloud.discoveryengine.v1beta.Document]s to be deleted, set [PurgeDocumentsRequest.force][google.cloud.discoveryengine.v1beta.PurgeDocumentsRequest.force] to false.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PurgeDocumentsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[PurgeDocumentsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsResponse)[PurgeDocumentsMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.PurgeDocumentsMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    PurgeDocumentsRequest request = new PurgeDocumentsRequest
    {
        ParentAsBranchName = BranchName.FromProjectLocationDataStoreBranch("[PROJECT]", "[LOCATION]", "[DATA_STORE]", "[BRANCH]"),
        Filter = "",
        Force = false,
        GcsSource = new GcsSource(),
        ErrorConfig = new PurgeErrorConfig(),
    };
    // Make the request
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> response = await documentServiceClient.PurgeDocumentsAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    PurgeDocumentsResponse result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<PurgeDocumentsResponse, PurgeDocumentsMetadata> retrievedResponse = await documentServiceClient.PollOncePurgeDocumentsAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        PurgeDocumentsResponse retrievedResult = retrievedResponse.Result;
    }
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_DocumentServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_DocumentServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_DocumentServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.DocumentServiceClient#Google_Cloud_DiscoveryEngine_V1Beta_DocumentServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateDocument(Document, FieldMask, CallSettings)
    
    
    public virtual Document UpdateDocument(Document document, FieldMask updateMask, CallSettings callSettings = null)

Updates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The document to update/create. If the caller does not have permission to update the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to update does not exist and [allow_missing][google.cloud.discoveryengine.v1beta.UpdateDocumentRequest.allow_missing] is not set, a `NOT_FOUND` error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    Document document = new Document();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Document response = documentServiceClient.UpdateDocument(document, updateMask);
    

### UpdateDocument(UpdateDocumentRequest, CallSettings)
    
    
    public virtual Document UpdateDocument(UpdateDocumentRequest request, CallSettings callSettings = null)

Updates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | The RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = DocumentServiceClient.Create();
    // Initialize request argument(s)
    UpdateDocumentRequest request = new UpdateDocumentRequest
    {
        Document = new Document(),
        AllowMissing = false,
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Document response = documentServiceClient.UpdateDocument(request);
    

### UpdateDocumentAsync(Document, FieldMask, CallSettings)
    
    
    public virtual Task<Document> UpdateDocumentAsync(Document document, FieldMask updateMask, CallSettings callSettings = null)

Updates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The document to update/create. If the caller does not have permission to update the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to update does not exist and [allow_missing][google.cloud.discoveryengine.v1beta.UpdateDocumentRequest.allow_missing] is not set, a `NOT_FOUND` error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Document document = new Document();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Document response = await documentServiceClient.UpdateDocumentAsync(document, updateMask);
    

### UpdateDocumentAsync(Document, FieldMask, CancellationToken)
    
    
    public virtual Task<Document> UpdateDocumentAsync(Document document, FieldMask updateMask, CancellationToken cancellationToken)

Updates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`document` | `[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)`  
Required. The document to update/create. If the caller does not have permission to update the [Document][google.cloud.discoveryengine.v1beta.Document], regardless of whether or not it exists, a `PERMISSION_DENIED` error is returned. If the [Document][google.cloud.discoveryengine.v1beta.Document] to update does not exist and [allow_missing][google.cloud.discoveryengine.v1beta.UpdateDocumentRequest.allow_missing] is not set, a `NOT_FOUND` error is returned.  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Indicates which fields in the provided imported 'document' to update. If not set, by default updates all fields.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    Document document = new Document();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Document response = await documentServiceClient.UpdateDocumentAsync(document, updateMask);
    

### UpdateDocumentAsync(UpdateDocumentRequest, CallSettings)
    
    
    public virtual Task<Document> UpdateDocumentAsync(UpdateDocumentRequest request, CallSettings callSettings = null)

Updates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDocumentRequest request = new UpdateDocumentRequest
    {
        Document = new Document(),
        AllowMissing = false,
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Document response = await documentServiceClient.UpdateDocumentAsync(request);
    

### UpdateDocumentAsync(UpdateDocumentRequest, CancellationToken)
    
    
    public virtual Task<Document> UpdateDocumentAsync(UpdateDocumentRequest request, CancellationToken cancellationToken)

Updates a [Document][google.cloud.discoveryengine.v1beta.Document].

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateDocumentRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.UpdateDocumentRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Document](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1Beta/latest/Google.Cloud.DiscoveryEngine.V1Beta.Document)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    DocumentServiceClient documentServiceClient = await DocumentServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateDocumentRequest request = new UpdateDocumentRequest
    {
        Document = new Document(),
        AllowMissing = false,
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Document response = await documentServiceClient.UpdateDocumentAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
