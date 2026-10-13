---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient
title: Dialogflow v3 API - Class ChangelogsClient (3.2.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:55.306973+00:00
---

# Dialogflow v3 API - Class ChangelogsClient (3.2.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Dialogflow v3 API - Class ChangelogsClient (3.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.2.0 (latest)  3.1.0  3.0.0  2.25.0  2.24.0  2.23.0  2.22.0  2.21.0  2.20.0  2.19.0  2.18.0  2.17.0  2.16.0  2.15.0  2.14.0  2.13.0  2.12.0  2.11.0  2.10.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class ChangelogsClient

Reference documentation and code samples for the Dialogflow v3 API class ChangelogsClient.

Changelogs client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChangelogsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ChangelogsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.Cx.V3](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3)

## Assembly

Google.Cloud.Dialogflow.Cx.V3.dll

## Remarks

Service for managing [Changelogs][google.cloud.dialogflow.cx.v3.Changelog].

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Changelogs service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Changelogs scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Changelogs scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### GrpcClient
    
    
    public virtual Changelogs.ChangelogsClient GrpcClient { get; }

The underlying gRPC Changelogs client

**Property Value**  
---  
**Type** | **Description**  
`[Changelogs](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelogs)[ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelogs.ChangelogsClient)` |   
  
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
    
    
    public static ChangelogsClient Create()

Synchronously creates a [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ChangelogsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient)` | The created [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ChangelogsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ChangelogsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient)` | The task representing the created [ChangelogsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient).  
  
### GetChangelog(ChangelogName, CallSettings)
    
    
    public virtual Changelog GetChangelog(ChangelogName name, CallSettings callSettings = null)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogName)`  
Required. The name of the changelog to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | The RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = ChangelogsClient.Create();
    // Initialize request argument(s)
    ChangelogName name = ChangelogName.FromProjectLocationAgentChangelog("[PROJECT]", "[LOCATION]", "[AGENT]", "[CHANGELOG]");
    // Make the request
    Changelog response = changelogsClient.GetChangelog(name);
    

### GetChangelog(GetChangelogRequest, CallSettings)
    
    
    public virtual Changelog GetChangelog(GetChangelogRequest request, CallSettings callSettings = null)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | The RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = ChangelogsClient.Create();
    // Initialize request argument(s)
    GetChangelogRequest request = new GetChangelogRequest
    {
        ChangelogName = ChangelogName.FromProjectLocationAgentChangelog("[PROJECT]", "[LOCATION]", "[AGENT]", "[CHANGELOG]"),
    };
    // Make the request
    Changelog response = changelogsClient.GetChangelog(request);
    

### GetChangelog(string, CallSettings)
    
    
    public virtual Changelog GetChangelog(string name, CallSettings callSettings = null)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the changelog to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | The RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = ChangelogsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/changelogs/[CHANGELOG]";
    // Make the request
    Changelog response = changelogsClient.GetChangelog(name);
    

### GetChangelogAsync(ChangelogName, CallSettings)
    
    
    public virtual Task<Changelog> GetChangelogAsync(ChangelogName name, CallSettings callSettings = null)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogName)`  
Required. The name of the changelog to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    ChangelogName name = ChangelogName.FromProjectLocationAgentChangelog("[PROJECT]", "[LOCATION]", "[AGENT]", "[CHANGELOG]");
    // Make the request
    Changelog response = await changelogsClient.GetChangelogAsync(name);
    

### GetChangelogAsync(ChangelogName, CancellationToken)
    
    
    public virtual Task<Changelog> GetChangelogAsync(ChangelogName name, CancellationToken cancellationToken)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ChangelogName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogName)`  
Required. The name of the changelog to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    ChangelogName name = ChangelogName.FromProjectLocationAgentChangelog("[PROJECT]", "[LOCATION]", "[AGENT]", "[CHANGELOG]");
    // Make the request
    Changelog response = await changelogsClient.GetChangelogAsync(name);
    

### GetChangelogAsync(GetChangelogRequest, CallSettings)
    
    
    public virtual Task<Changelog> GetChangelogAsync(GetChangelogRequest request, CallSettings callSettings = null)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    GetChangelogRequest request = new GetChangelogRequest
    {
        ChangelogName = ChangelogName.FromProjectLocationAgentChangelog("[PROJECT]", "[LOCATION]", "[AGENT]", "[CHANGELOG]"),
    };
    // Make the request
    Changelog response = await changelogsClient.GetChangelogAsync(request);
    

### GetChangelogAsync(GetChangelogRequest, CancellationToken)
    
    
    public virtual Task<Changelog> GetChangelogAsync(GetChangelogRequest request, CancellationToken cancellationToken)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetChangelogRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.GetChangelogRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    GetChangelogRequest request = new GetChangelogRequest
    {
        ChangelogName = ChangelogName.FromProjectLocationAgentChangelog("[PROJECT]", "[LOCATION]", "[AGENT]", "[CHANGELOG]"),
    };
    // Make the request
    Changelog response = await changelogsClient.GetChangelogAsync(request);
    

### GetChangelogAsync(string, CallSettings)
    
    
    public virtual Task<Changelog> GetChangelogAsync(string name, CallSettings callSettings = null)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the changelog to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/changelogs/[CHANGELOG]";
    // Make the request
    Changelog response = await changelogsClient.GetChangelogAsync(name);
    

### GetChangelogAsync(string, CancellationToken)
    
    
    public virtual Task<Changelog> GetChangelogAsync(string name, CancellationToken cancellationToken)

Retrieves the specified Changelog.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the changelog to get. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/changelogs/<ChangelogID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]/changelogs/[CHANGELOG]";
    // Make the request
    Changelog response = await changelogsClient.GetChangelogAsync(name);
    

### ListChangelogs(AgentName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListChangelogsResponse, Changelog> ListChangelogs(AgentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of Changelogs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent containing the changelogs. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A pageable sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog) resources.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = ChangelogsClient.Create();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    PagedEnumerable<ListChangelogsResponse, Changelog> response = changelogsClient.ListChangelogs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogs(ListChangelogsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListChangelogsResponse, Changelog> ListChangelogs(ListChangelogsRequest request, CallSettings callSettings = null)

Returns the list of Changelogs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A pageable sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog) resources.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = ChangelogsClient.Create();
    // Initialize request argument(s)
    ListChangelogsRequest request = new ListChangelogsRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListChangelogsResponse, Changelog> response = changelogsClient.ListChangelogs(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogs(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListChangelogsResponse, Changelog> ListChangelogs(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of Changelogs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent containing the changelogs. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A pageable sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog) resources.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = ChangelogsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    PagedEnumerable<ListChangelogsResponse, Changelog> response = changelogsClient.ListChangelogs(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogsAsync(AgentName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListChangelogsResponse, Changelog> ListChangelogsAsync(AgentName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of Changelogs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[AgentName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.AgentName)`  
Required. The agent containing the changelogs. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A pageable asynchronous sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog) resources.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    AgentName parent = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]");
    // Make the request
    PagedAsyncEnumerable<ListChangelogsResponse, Changelog> response = changelogsClient.ListChangelogsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogsAsync(ListChangelogsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListChangelogsResponse, Changelog> ListChangelogsAsync(ListChangelogsRequest request, CallSettings callSettings = null)

Returns the list of Changelogs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListChangelogsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A pageable asynchronous sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog) resources.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    ListChangelogsRequest request = new ListChangelogsRequest
    {
        ParentAsAgentName = AgentName.FromProjectLocationAgent("[PROJECT]", "[LOCATION]", "[AGENT]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListChangelogsResponse, Changelog> response = changelogsClient.ListChangelogsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListChangelogsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListChangelogsResponse, Changelog> ListChangelogsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of Changelogs.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The agent containing the changelogs. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListChangelogsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ListChangelogsResponse)[Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog)` | A pageable asynchronous sequence of [Changelog](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.Changelog) resources.  
**Example**
    
    
    // Create client
    ChangelogsClient changelogsClient = await ChangelogsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]/agents/[AGENT]";
    // Make the request
    PagedAsyncEnumerable<ListChangelogsResponse, Changelog> response = changelogsClient.ListChangelogsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Changelog item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListChangelogsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Changelog item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Changelog> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Changelog item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient#Google_Cloud_Dialogflow_Cx_V3_ChangelogsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient#Google_Cloud_Dialogflow_Cx_V3_ChangelogsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient#Google_Cloud_Dialogflow_Cx_V3_ChangelogsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.Cx.V3/latest/Google.Cloud.Dialogflow.Cx.V3.ChangelogsClient#Google_Cloud_Dialogflow_Cx_V3_ChangelogsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
