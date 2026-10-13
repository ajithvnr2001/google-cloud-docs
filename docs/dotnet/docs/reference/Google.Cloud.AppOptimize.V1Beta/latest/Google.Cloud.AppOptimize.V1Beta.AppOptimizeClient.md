---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient
title: App Optimize v1beta API - Class AppOptimizeClient (1.0.0-beta01) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:18:10.941673+00:00
---

# App Optimize v1beta API - Class AppOptimizeClient (1.0.0-beta01)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  App Optimize v1beta API - Class AppOptimizeClient (1.0.0-beta01) Stay organized with collections  Save and categorize content based on your preferences. 
    
    
    public abstract class AppOptimizeClient

Reference documentation and code samples for the App Optimize v1beta API class AppOptimizeClient.

AppOptimize client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AppOptimizeClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[AppOptimizeClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClientImpl)

## Namespace

[Google.Cloud.AppOptimize.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta)

## Assembly

Google.Cloud.AppOptimize.V1Beta.dll

## Remarks

Service for managing and querying optimization reports.

## Properties 

### CreateReportOperationsClient
    
    
    public virtual OperationsClient CreateReportOperationsClient { get; }

The long-running operations client for `CreateReport`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the AppOptimize service, which is a host of "appoptimize.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default AppOptimize scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default AppOptimize scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual AppOptimize.AppOptimizeClient GrpcClient { get; }

The underlying gRPC AppOptimize client

**Property Value**  
---  
**Type** | **Description**  
`[AppOptimize](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimize)[AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimize.AppOptimizeClient)` |   
  
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
    
    
    public static AppOptimizeClient Create()

Synchronously creates a [AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AppOptimizeClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient)` | The created [AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<AppOptimizeClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [AppOptimizeClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient)` | The task representing the created [AppOptimizeClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient).  
  
### CreateReport(LocationName, Report, string, CallSettings)
    
    
    public virtual Operation<Report, OperationMetadata> CreateReport(LocationName parent, Report report, string reportId, CallSettings callSettings = null)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent Google Cloud project that will own the report. This value does not define the scope of the report data. See `Report.scope` for setting the data scope. Format: `projects/{project}/locations/{location}`.  
`report` | `[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)`  
Required. The report resource to create.  
`reportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Report report = new Report();
    string reportId = "";
    // Make the request
    Operation<Report, OperationMetadata> response = appOptimizeClient.CreateReport(parent, report, reportId);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = appOptimizeClient.PollOnceCreateReport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReport(CreateReportRequest, CallSettings)
    
    
    public virtual Operation<Report, OperationMetadata> CreateReport(CreateReportRequest request, CallSettings callSettings = null)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.CreateReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    CreateReportRequest request = new CreateReportRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReportId = "",
        Report = new Report(),
    };
    // Make the request
    Operation<Report, OperationMetadata> response = appOptimizeClient.CreateReport(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = appOptimizeClient.PollOnceCreateReport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReport(string, Report, string, CallSettings)
    
    
    public virtual Operation<Report, OperationMetadata> CreateReport(string parent, Report report, string reportId, CallSettings callSettings = null)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Google Cloud project that will own the report. This value does not define the scope of the report data. See `Report.scope` for setting the data scope. Format: `projects/{project}/locations/{location}`.  
`report` | `[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)`  
Required. The report resource to create.  
`reportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Report report = new Report();
    string reportId = "";
    // Make the request
    Operation<Report, OperationMetadata> response = appOptimizeClient.CreateReport(parent, report, reportId);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = appOptimizeClient.PollOnceCreateReport(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReportAsync(LocationName, Report, string, CallSettings)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> CreateReportAsync(LocationName parent, Report report, string reportId, CallSettings callSettings = null)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent Google Cloud project that will own the report. This value does not define the scope of the report data. See `Report.scope` for setting the data scope. Format: `projects/{project}/locations/{location}`.  
`report` | `[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)`  
Required. The report resource to create.  
`reportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Report report = new Report();
    string reportId = "";
    // Make the request
    Operation<Report, OperationMetadata> response = await appOptimizeClient.CreateReportAsync(parent, report, reportId);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = await appOptimizeClient.PollOnceCreateReportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReportAsync(LocationName, Report, string, CancellationToken)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> CreateReportAsync(LocationName parent, Report report, string reportId, CancellationToken cancellationToken)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent Google Cloud project that will own the report. This value does not define the scope of the report data. See `Report.scope` for setting the data scope. Format: `projects/{project}/locations/{location}`.  
`report` | `[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)`  
Required. The report resource to create.  
`reportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Report report = new Report();
    string reportId = "";
    // Make the request
    Operation<Report, OperationMetadata> response = await appOptimizeClient.CreateReportAsync(parent, report, reportId);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = await appOptimizeClient.PollOnceCreateReportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReportAsync(CreateReportRequest, CallSettings)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> CreateReportAsync(CreateReportRequest request, CallSettings callSettings = null)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.CreateReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    CreateReportRequest request = new CreateReportRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReportId = "",
        Report = new Report(),
    };
    // Make the request
    Operation<Report, OperationMetadata> response = await appOptimizeClient.CreateReportAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = await appOptimizeClient.PollOnceCreateReportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReportAsync(CreateReportRequest, CancellationToken)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> CreateReportAsync(CreateReportRequest request, CancellationToken cancellationToken)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.CreateReportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    CreateReportRequest request = new CreateReportRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        ReportId = "",
        Report = new Report(),
    };
    // Make the request
    Operation<Report, OperationMetadata> response = await appOptimizeClient.CreateReportAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = await appOptimizeClient.PollOnceCreateReportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReportAsync(string, Report, string, CallSettings)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> CreateReportAsync(string parent, Report report, string reportId, CallSettings callSettings = null)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Google Cloud project that will own the report. This value does not define the scope of the report data. See `Report.scope` for setting the data scope. Format: `projects/{project}/locations/{location}`.  
`report` | `[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)`  
Required. The report resource to create.  
`reportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Report report = new Report();
    string reportId = "";
    // Make the request
    Operation<Report, OperationMetadata> response = await appOptimizeClient.CreateReportAsync(parent, report, reportId);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = await appOptimizeClient.PollOnceCreateReportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### CreateReportAsync(string, Report, string, CancellationToken)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> CreateReportAsync(string parent, Report report, string reportId, CancellationToken cancellationToken)

Creates a new report.

This initiates a long-running operation that, upon completion, results in a report resource. Once the report is created, its results can be read via `ReadReport`.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent Google Cloud project that will own the report. This value does not define the scope of the report data. See `Report.scope` for setting the data scope. Format: `projects/{project}/locations/{location}`.  
`report` | `[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)`  
Required. The report resource to create.  
`reportId` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The ID to use for this report. This ID must be unique within the parent project and should comply with RFC 1034 restrictions (letters, numbers, and hyphen, with the first character a letter, the last a letter or a number, and a 63 character maximum).  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Report report = new Report();
    string reportId = "";
    // Make the request
    Operation<Report, OperationMetadata> response = await appOptimizeClient.CreateReportAsync(parent, report, reportId);
    
    // Poll until the returned long-running operation is complete
    Operation<Report, OperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Report result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Report, OperationMetadata> retrievedResponse = await appOptimizeClient.PollOnceCreateReportAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Report retrievedResult = retrievedResponse.Result;
    }
    

### DeleteReport(DeleteReportRequest, CallSettings)
    
    
    public virtual void DeleteReport(DeleteReportRequest request, CallSettings callSettings = null)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.DeleteReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    DeleteReportRequest request = new DeleteReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
        AllowMissing = false,
    };
    // Make the request
    appOptimizeClient.DeleteReport(request);
    

### DeleteReport(ReportName, CallSettings)
    
    
    public virtual void DeleteReport(ReportName name, CallSettings callSettings = null)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The name of the report to delete. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    appOptimizeClient.DeleteReport(name);
    

### DeleteReport(string, CallSettings)
    
    
    public virtual void DeleteReport(string name, CallSettings callSettings = null)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the report to delete. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    appOptimizeClient.DeleteReport(name);
    

### DeleteReportAsync(DeleteReportRequest, CallSettings)
    
    
    public virtual Task DeleteReportAsync(DeleteReportRequest request, CallSettings callSettings = null)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.DeleteReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    DeleteReportRequest request = new DeleteReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
        AllowMissing = false,
    };
    // Make the request
    await appOptimizeClient.DeleteReportAsync(request);
    

### DeleteReportAsync(DeleteReportRequest, CancellationToken)
    
    
    public virtual Task DeleteReportAsync(DeleteReportRequest request, CancellationToken cancellationToken)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.DeleteReportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    DeleteReportRequest request = new DeleteReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
        AllowMissing = false,
    };
    // Make the request
    await appOptimizeClient.DeleteReportAsync(request);
    

### DeleteReportAsync(ReportName, CallSettings)
    
    
    public virtual Task DeleteReportAsync(ReportName name, CallSettings callSettings = null)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The name of the report to delete. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    await appOptimizeClient.DeleteReportAsync(name);
    

### DeleteReportAsync(ReportName, CancellationToken)
    
    
    public virtual Task DeleteReportAsync(ReportName name, CancellationToken cancellationToken)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The name of the report to delete. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    await appOptimizeClient.DeleteReportAsync(name);
    

### DeleteReportAsync(string, CallSettings)
    
    
    public virtual Task DeleteReportAsync(string name, CallSettings callSettings = null)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the report to delete. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    await appOptimizeClient.DeleteReportAsync(name);
    

### DeleteReportAsync(string, CancellationToken)
    
    
    public virtual Task DeleteReportAsync(string name, CancellationToken cancellationToken)

Deletes the specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the report to delete. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    await appOptimizeClient.DeleteReportAsync(name);
    

### GetReport(GetReportRequest, CallSettings)
    
    
    public virtual Report GetReport(GetReportRequest request, CallSettings callSettings = null)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.GetReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | The RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    GetReportRequest request = new GetReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
    };
    // Make the request
    Report response = appOptimizeClient.GetReport(request);
    

### GetReport(ReportName, CallSettings)
    
    
    public virtual Report GetReport(ReportName name, CallSettings callSettings = null)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The name of the report to retrieve. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | The RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    Report response = appOptimizeClient.GetReport(name);
    

### GetReport(string, CallSettings)
    
    
    public virtual Report GetReport(string name, CallSettings callSettings = null)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the report to retrieve. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | The RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    Report response = appOptimizeClient.GetReport(name);
    

### GetReportAsync(GetReportRequest, CallSettings)
    
    
    public virtual Task<Report> GetReportAsync(GetReportRequest request, CallSettings callSettings = null)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.GetReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    GetReportRequest request = new GetReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
    };
    // Make the request
    Report response = await appOptimizeClient.GetReportAsync(request);
    

### GetReportAsync(GetReportRequest, CancellationToken)
    
    
    public virtual Task<Report> GetReportAsync(GetReportRequest request, CancellationToken cancellationToken)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.GetReportRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    GetReportRequest request = new GetReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
    };
    // Make the request
    Report response = await appOptimizeClient.GetReportAsync(request);
    

### GetReportAsync(ReportName, CallSettings)
    
    
    public virtual Task<Report> GetReportAsync(ReportName name, CallSettings callSettings = null)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The name of the report to retrieve. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    Report response = await appOptimizeClient.GetReportAsync(name);
    

### GetReportAsync(ReportName, CancellationToken)
    
    
    public virtual Task<Report> GetReportAsync(ReportName name, CancellationToken cancellationToken)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The name of the report to retrieve. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    Report response = await appOptimizeClient.GetReportAsync(name);
    

### GetReportAsync(string, CallSettings)
    
    
    public virtual Task<Report> GetReportAsync(string name, CallSettings callSettings = null)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the report to retrieve. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    Report response = await appOptimizeClient.GetReportAsync(name);
    

### GetReportAsync(string, CancellationToken)
    
    
    public virtual Task<Report> GetReportAsync(string name, CancellationToken cancellationToken)

Retrieves the details of a report configuration.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the report to retrieve. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    Report response = await appOptimizeClient.GetReportAsync(name);
    

### ListReports(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListReportsResponse, Report> ListReports(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project whose reports are to be listed. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A pageable sequence of [Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListReportsResponse, Report> response = appOptimizeClient.ListReports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Report item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Report item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Report> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Report item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReports(ListReportsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListReportsResponse, Report> ListReports(ListReportsRequest request, CallSettings callSettings = null)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A pageable sequence of [Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    ListReportsRequest request = new ListReportsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedEnumerable<ListReportsResponse, Report> response = appOptimizeClient.ListReports(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Report item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Report item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Report> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Report item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReports(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListReportsResponse, Report> ListReports(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project whose reports are to be listed. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A pageable sequence of [Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListReportsResponse, Report> response = appOptimizeClient.ListReports(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Report item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Report item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Report> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Report item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReportsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReportsResponse, Report> ListReportsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The parent project whose reports are to be listed. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A pageable asynchronous sequence of [Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListReportsResponse, Report> response = appOptimizeClient.ListReportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Report item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Report item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Report> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Report item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReportsAsync(ListReportsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReportsResponse, Report> ListReportsAsync(ListReportsRequest request, CallSettings callSettings = null)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListReportsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A pageable asynchronous sequence of [Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ListReportsRequest request = new ListReportsRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
    };
    // Make the request
    PagedAsyncEnumerable<ListReportsResponse, Report> response = appOptimizeClient.ListReportsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Report item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Report item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Report> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Report item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListReportsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListReportsResponse, Report> ListReportsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists reports within a given project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The parent project whose reports are to be listed. Format: `projects/{project}/locations/{location}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListReportsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ListReportsResponse)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)` | A pageable asynchronous sequence of [Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListReportsResponse, Report> response = appOptimizeClient.ListReportsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Report item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListReportsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Report item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Report> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Report item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PollOnceCreateReport(string, CallSettings)
    
    
    public virtual Operation<Report, OperationMetadata> PollOnceCreateReport(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `CreateReport`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | The result of polling the operation.  
  
### PollOnceCreateReportAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Report, OperationMetadata>> PollOnceCreateReportAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `CreateReport`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Report](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.Report)[OperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.OperationMetadata)` | A task representing the result of polling the operation.  
  
### ReadReport(ReadReportRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ReadReportResponse, ListValue> ReadReport(ReadReportRequest request, CallSettings callSettings = null)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` | A pageable sequence of [ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    ReadReportRequest request = new ReadReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
    };
    // Make the request
    PagedEnumerable<ReadReportResponse, ListValue> response = appOptimizeClient.ReadReport(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ListValue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ReadReportResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ListValue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ListValue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ListValue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ReadReport(ReportName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ReadReportResponse, ListValue> ReadReport(ReportName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The resource name of the report to query. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` | A pageable sequence of [ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    PagedEnumerable<ReadReportResponse, ListValue> response = appOptimizeClient.ReadReport(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ListValue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ReadReportResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ListValue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ListValue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ListValue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ReadReport(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ReadReportResponse, ListValue> ReadReport(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the report to query. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` | A pageable sequence of [ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = AppOptimizeClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    PagedEnumerable<ReadReportResponse, ListValue> response = appOptimizeClient.ReadReport(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (ListValue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ReadReportResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ListValue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ListValue> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ListValue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ReadReportAsync(ReadReportRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ReadReportResponse, ListValue> ReadReportAsync(ReadReportRequest request, CallSettings callSettings = null)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ReadReportRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` | A pageable asynchronous sequence of [ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ReadReportRequest request = new ReadReportRequest
    {
        ReportName = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]"),
    };
    // Make the request
    PagedAsyncEnumerable<ReadReportResponse, ListValue> response = appOptimizeClient.ReadReportAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ListValue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ReadReportResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ListValue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ListValue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ListValue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ReadReportAsync(ReportName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ReadReportResponse, ListValue> ReadReportAsync(ReportName name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ReportName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReportName)`  
Required. The resource name of the report to query. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` | A pageable asynchronous sequence of [ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    ReportName name = ReportName.FromProjectLocationReport("[PROJECT]", "[LOCATION]", "[REPORT]");
    // Make the request
    PagedAsyncEnumerable<ReadReportResponse, ListValue> response = appOptimizeClient.ReadReportAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ListValue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ReadReportResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ListValue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ListValue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ListValue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ReadReportAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ReadReportResponse, ListValue> ReadReportAsync(string name, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Reads data within a specified report.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the report to query. Format: `projects/{project}/locations/{location}/reports/{report_id}`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ReadReportResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.ReadReportResponse)[ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html)` | A pageable asynchronous sequence of [ListValue](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.ListValue.html) resources.  
**Example**
    
    
    // Create client
    AppOptimizeClient appOptimizeClient = await AppOptimizeClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/reports/[REPORT]";
    // Make the request
    PagedAsyncEnumerable<ReadReportResponse, ListValue> response = appOptimizeClient.ReadReportAsync(name);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (ListValue item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ReadReportResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (ListValue item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<ListValue> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (ListValue item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient#Google_Cloud_AppOptimize_V1Beta_AppOptimizeClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient#Google_Cloud_AppOptimize_V1Beta_AppOptimizeClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient#Google_Cloud_AppOptimize_V1Beta_AppOptimizeClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AppOptimize.V1Beta/latest/Google.Cloud.AppOptimize.V1Beta.AppOptimizeClient#Google_Cloud_AppOptimize_V1Beta_AppOptimizeClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-23 UTC."],[],[]] 
