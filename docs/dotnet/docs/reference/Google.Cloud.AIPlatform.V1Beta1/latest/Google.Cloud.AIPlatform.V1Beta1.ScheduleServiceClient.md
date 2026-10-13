---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient
title: Vertex AI v1beta1 API - Class ScheduleServiceClient (1.0.0-beta87) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:11:43.077388+00:00
---

# Vertex AI v1beta1 API - Class ScheduleServiceClient (1.0.0-beta87)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vertex AI v1beta1 API - Class ScheduleServiceClient (1.0.0-beta87) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta87 (latest)  1.0.0-beta86 
    
    
    public abstract class ScheduleServiceClient

Reference documentation and code samples for the Vertex AI v1beta1 API class ScheduleServiceClient.

ScheduleService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ScheduleServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ScheduleServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClientImpl)

## Namespace

[Google.Cloud.AIPlatform.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1)

## Assembly

Google.Cloud.AIPlatform.V1Beta1.dll

## Remarks

A service for creating and managing Vertex AI's Schedule resources to periodically launch shceudled runs to make API calls.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ScheduleService service, which is a host of "aiplatform.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ScheduleService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ScheduleService scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### DeleteScheduleOperationsClient
    
    
    public virtual OperationsClient DeleteScheduleOperationsClient { get; }

The long-running operations client for `DeleteSchedule`.

**Property Value**  
---  
**Type** | **Description**  
`[OperationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.OperationsClient.html)` |   
  
### GrpcClient
    
    
    public virtual ScheduleService.ScheduleServiceClient GrpcClient { get; }

The underlying gRPC ScheduleService client

**Property Value**  
---  
**Type** | **Description**  
`[ScheduleService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleService)[ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleService.ScheduleServiceClient)` |   
  
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
  
## Methods 

### Create()
    
    
    public static ScheduleServiceClient Create()

Synchronously creates a [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ScheduleServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient)` | The created [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ScheduleServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ScheduleServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient)` | The task representing the created [ScheduleServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient).  
  
### CreateSchedule(LocationName, Schedule, CallSettings)
    
    
    public virtual Schedule CreateSchedule(LocationName parent, Schedule schedule, CallSettings callSettings = null)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Schedule schedule = new Schedule();
    // Make the request
    Schedule response = scheduleServiceClient.CreateSchedule(parent, schedule);
    

### CreateSchedule(CreateScheduleRequest, CallSettings)
    
    
    public virtual Schedule CreateSchedule(CreateScheduleRequest request, CallSettings callSettings = null)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    CreateScheduleRequest request = new CreateScheduleRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Schedule = new Schedule(),
    };
    // Make the request
    Schedule response = scheduleServiceClient.CreateSchedule(request);
    

### CreateSchedule(string, Schedule, CallSettings)
    
    
    public virtual Schedule CreateSchedule(string parent, Schedule schedule, CallSettings callSettings = null)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Schedule schedule = new Schedule();
    // Make the request
    Schedule response = scheduleServiceClient.CreateSchedule(parent, schedule);
    

### CreateScheduleAsync(LocationName, Schedule, CallSettings)
    
    
    public virtual Task<Schedule> CreateScheduleAsync(LocationName parent, Schedule schedule, CallSettings callSettings = null)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Schedule schedule = new Schedule();
    // Make the request
    Schedule response = await scheduleServiceClient.CreateScheduleAsync(parent, schedule);
    

### CreateScheduleAsync(LocationName, Schedule, CancellationToken)
    
    
    public virtual Task<Schedule> CreateScheduleAsync(LocationName parent, Schedule schedule, CancellationToken cancellationToken)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Schedule schedule = new Schedule();
    // Make the request
    Schedule response = await scheduleServiceClient.CreateScheduleAsync(parent, schedule);
    

### CreateScheduleAsync(CreateScheduleRequest, CallSettings)
    
    
    public virtual Task<Schedule> CreateScheduleAsync(CreateScheduleRequest request, CallSettings callSettings = null)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateScheduleRequest request = new CreateScheduleRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Schedule = new Schedule(),
    };
    // Make the request
    Schedule response = await scheduleServiceClient.CreateScheduleAsync(request);
    

### CreateScheduleAsync(CreateScheduleRequest, CancellationToken)
    
    
    public virtual Task<Schedule> CreateScheduleAsync(CreateScheduleRequest request, CancellationToken cancellationToken)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.CreateScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    CreateScheduleRequest request = new CreateScheduleRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Schedule = new Schedule(),
    };
    // Make the request
    Schedule response = await scheduleServiceClient.CreateScheduleAsync(request);
    

### CreateScheduleAsync(string, Schedule, CallSettings)
    
    
    public virtual Task<Schedule> CreateScheduleAsync(string parent, Schedule schedule, CallSettings callSettings = null)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Schedule schedule = new Schedule();
    // Make the request
    Schedule response = await scheduleServiceClient.CreateScheduleAsync(parent, schedule);
    

### CreateScheduleAsync(string, Schedule, CancellationToken)
    
    
    public virtual Task<Schedule> CreateScheduleAsync(string parent, Schedule schedule, CancellationToken cancellationToken)

Creates a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to create the Schedule in. Format: `projects/{project}/locations/{location}`  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Schedule schedule = new Schedule();
    // Make the request
    Schedule response = await scheduleServiceClient.CreateScheduleAsync(parent, schedule);
    

### DeleteSchedule(DeleteScheduleRequest, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteSchedule(DeleteScheduleRequest request, CallSettings callSettings = null)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    DeleteScheduleRequest request = new DeleteScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = scheduleServiceClient.DeleteSchedule(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = scheduleServiceClient.PollOnceDeleteSchedule(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSchedule(ScheduleName, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteSchedule(ScheduleName name, CallSettings callSettings = null)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = scheduleServiceClient.DeleteSchedule(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = scheduleServiceClient.PollOnceDeleteSchedule(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteSchedule(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> DeleteSchedule(string name, CallSettings callSettings = null)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = scheduleServiceClient.DeleteSchedule(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = response.PollUntilCompleted();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = scheduleServiceClient.PollOnceDeleteSchedule(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteScheduleAsync(DeleteScheduleRequest, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteScheduleAsync(DeleteScheduleRequest request, CallSettings callSettings = null)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteScheduleRequest request = new DeleteScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await scheduleServiceClient.DeleteScheduleAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await scheduleServiceClient.PollOnceDeleteScheduleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteScheduleAsync(DeleteScheduleRequest, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteScheduleAsync(DeleteScheduleRequest request, CancellationToken cancellationToken)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[DeleteScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    DeleteScheduleRequest request = new DeleteScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await scheduleServiceClient.DeleteScheduleAsync(request);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await scheduleServiceClient.PollOnceDeleteScheduleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteScheduleAsync(ScheduleName, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteScheduleAsync(ScheduleName name, CallSettings callSettings = null)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await scheduleServiceClient.DeleteScheduleAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await scheduleServiceClient.PollOnceDeleteScheduleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteScheduleAsync(ScheduleName, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteScheduleAsync(ScheduleName name, CancellationToken cancellationToken)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await scheduleServiceClient.DeleteScheduleAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await scheduleServiceClient.PollOnceDeleteScheduleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteScheduleAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteScheduleAsync(string name, CallSettings callSettings = null)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await scheduleServiceClient.DeleteScheduleAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await scheduleServiceClient.PollOnceDeleteScheduleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### DeleteScheduleAsync(string, CancellationToken)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> DeleteScheduleAsync(string name, CancellationToken cancellationToken)

Deletes a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be deleted. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    Operation<Empty, DeleteOperationMetadata> response = await scheduleServiceClient.DeleteScheduleAsync(name);
    
    // Poll until the returned long-running operation is complete
    Operation<Empty, DeleteOperationMetadata> completedResponse = await response.PollUntilCompletedAsync();
    // Retrieve the operation result
    Empty result = completedResponse.Result;
    
    // Or get the name of the operation
    string operationName = response.Name;
    // This name can be stored, then the long-running operation retrieved later by name
    Operation<Empty, DeleteOperationMetadata> retrievedResponse = await scheduleServiceClient.PollOnceDeleteScheduleAsync(operationName);
    // Check if the retrieved long-running operation has completed
    if (retrievedResponse.IsCompleted)
    {
        // If it has completed, then access the result
        Empty retrievedResult = retrievedResponse.Result;
    }
    

### GetSchedule(GetScheduleRequest, CallSettings)
    
    
    public virtual Schedule GetSchedule(GetScheduleRequest request, CallSettings callSettings = null)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    GetScheduleRequest request = new GetScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    Schedule response = scheduleServiceClient.GetSchedule(request);
    

### GetSchedule(ScheduleName, CallSettings)
    
    
    public virtual Schedule GetSchedule(ScheduleName name, CallSettings callSettings = null)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    Schedule response = scheduleServiceClient.GetSchedule(name);
    

### GetSchedule(string, CallSettings)
    
    
    public virtual Schedule GetSchedule(string name, CallSettings callSettings = null)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    Schedule response = scheduleServiceClient.GetSchedule(name);
    

### GetScheduleAsync(GetScheduleRequest, CallSettings)
    
    
    public virtual Task<Schedule> GetScheduleAsync(GetScheduleRequest request, CallSettings callSettings = null)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetScheduleRequest request = new GetScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    Schedule response = await scheduleServiceClient.GetScheduleAsync(request);
    

### GetScheduleAsync(GetScheduleRequest, CancellationToken)
    
    
    public virtual Task<Schedule> GetScheduleAsync(GetScheduleRequest request, CancellationToken cancellationToken)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.GetScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    GetScheduleRequest request = new GetScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    Schedule response = await scheduleServiceClient.GetScheduleAsync(request);
    

### GetScheduleAsync(ScheduleName, CallSettings)
    
    
    public virtual Task<Schedule> GetScheduleAsync(ScheduleName name, CallSettings callSettings = null)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    Schedule response = await scheduleServiceClient.GetScheduleAsync(name);
    

### GetScheduleAsync(ScheduleName, CancellationToken)
    
    
    public virtual Task<Schedule> GetScheduleAsync(ScheduleName name, CancellationToken cancellationToken)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    Schedule response = await scheduleServiceClient.GetScheduleAsync(name);
    

### GetScheduleAsync(string, CallSettings)
    
    
    public virtual Task<Schedule> GetScheduleAsync(string name, CallSettings callSettings = null)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    Schedule response = await scheduleServiceClient.GetScheduleAsync(name);
    

### GetScheduleAsync(string, CancellationToken)
    
    
    public virtual Task<Schedule> GetScheduleAsync(string name, CancellationToken cancellationToken)

Gets a Schedule.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    Schedule response = await scheduleServiceClient.GetScheduleAsync(name);
    

### ListSchedules(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSchedulesResponse, Schedule> ListSchedules(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Schedules in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list the Schedules from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSchedulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesResponse)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A pageable sequence of [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule) resources.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListSchedulesResponse, Schedule> response = scheduleServiceClient.ListSchedules(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Schedule item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSchedulesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Schedule item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Schedule> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Schedule item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSchedules(ListSchedulesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListSchedulesResponse, Schedule> ListSchedules(ListSchedulesRequest request, CallSettings callSettings = null)

Lists Schedules in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSchedulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSchedulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesResponse)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A pageable sequence of [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule) resources.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ListSchedulesRequest request = new ListSchedulesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedEnumerable<ListSchedulesResponse, Schedule> response = scheduleServiceClient.ListSchedules(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Schedule item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSchedulesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Schedule item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Schedule> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Schedule item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSchedules(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListSchedulesResponse, Schedule> ListSchedules(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Schedules in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list the Schedules from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListSchedulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesResponse)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A pageable sequence of [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule) resources.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedEnumerable<ListSchedulesResponse, Schedule> response = scheduleServiceClient.ListSchedules(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Schedule item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListSchedulesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Schedule item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Schedule> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Schedule item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSchedulesAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSchedulesResponse, Schedule> ListSchedulesAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Schedules in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the Location to list the Schedules from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSchedulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesResponse)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A pageable asynchronous sequence of [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule) resources.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListSchedulesResponse, Schedule> response = scheduleServiceClient.ListSchedulesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Schedule item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSchedulesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Schedule item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Schedule> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Schedule item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSchedulesAsync(ListSchedulesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSchedulesResponse, Schedule> ListSchedulesAsync(ListSchedulesRequest request, CallSettings callSettings = null)

Lists Schedules in a Location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListSchedulesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSchedulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesResponse)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A pageable asynchronous sequence of [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule) resources.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ListSchedulesRequest request = new ListSchedulesRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Filter = "",
        OrderBy = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListSchedulesResponse, Schedule> response = scheduleServiceClient.ListSchedulesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Schedule item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSchedulesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Schedule item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Schedule> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Schedule item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListSchedulesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListSchedulesResponse, Schedule> ListSchedulesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists Schedules in a Location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the Location to list the Schedules from. Format: `projects/{project}/locations/{location}`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListSchedulesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ListSchedulesResponse)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A pageable asynchronous sequence of [Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule) resources.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    // Make the request
    PagedAsyncEnumerable<ListSchedulesResponse, Schedule> response = scheduleServiceClient.ListSchedulesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Schedule item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListSchedulesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Schedule item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Schedule> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Schedule item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### PauseSchedule(PauseScheduleRequest, CallSettings)
    
    
    public virtual void PauseSchedule(PauseScheduleRequest request, CallSettings callSettings = null)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PauseScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    PauseScheduleRequest request = new PauseScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    scheduleServiceClient.PauseSchedule(request);
    

### PauseSchedule(ScheduleName, CallSettings)
    
    
    public virtual void PauseSchedule(ScheduleName name, CallSettings callSettings = null)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    scheduleServiceClient.PauseSchedule(name);
    

### PauseSchedule(string, CallSettings)
    
    
    public virtual void PauseSchedule(string name, CallSettings callSettings = null)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    scheduleServiceClient.PauseSchedule(name);
    

### PauseScheduleAsync(PauseScheduleRequest, CallSettings)
    
    
    public virtual Task PauseScheduleAsync(PauseScheduleRequest request, CallSettings callSettings = null)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PauseScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    PauseScheduleRequest request = new PauseScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    await scheduleServiceClient.PauseScheduleAsync(request);
    

### PauseScheduleAsync(PauseScheduleRequest, CancellationToken)
    
    
    public virtual Task PauseScheduleAsync(PauseScheduleRequest request, CancellationToken cancellationToken)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[PauseScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.PauseScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    PauseScheduleRequest request = new PauseScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
    };
    // Make the request
    await scheduleServiceClient.PauseScheduleAsync(request);
    

### PauseScheduleAsync(ScheduleName, CallSettings)
    
    
    public virtual Task PauseScheduleAsync(ScheduleName name, CallSettings callSettings = null)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    await scheduleServiceClient.PauseScheduleAsync(name);
    

### PauseScheduleAsync(ScheduleName, CancellationToken)
    
    
    public virtual Task PauseScheduleAsync(ScheduleName name, CancellationToken cancellationToken)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    await scheduleServiceClient.PauseScheduleAsync(name);
    

### PauseScheduleAsync(string, CallSettings)
    
    
    public virtual Task PauseScheduleAsync(string name, CallSettings callSettings = null)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    await scheduleServiceClient.PauseScheduleAsync(name);
    

### PauseScheduleAsync(string, CancellationToken)
    
    
    public virtual Task PauseScheduleAsync(string name, CancellationToken cancellationToken)

Pauses a Schedule. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'PAUSED'. If the schedule is paused, no new runs will be created. Already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be paused. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    await scheduleServiceClient.PauseScheduleAsync(name);
    

### PollOnceDeleteSchedule(string, CallSettings)
    
    
    public virtual Operation<Empty, DeleteOperationMetadata> PollOnceDeleteSchedule(string operationName, CallSettings callSettings = null)

Poll an operation once, using an `operationName` from a previous invocation of `DeleteSchedule`.

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
`[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | The result of polling the operation.  
  
### PollOnceDeleteScheduleAsync(string, CallSettings)
    
    
    public virtual Task<Operation<Empty, DeleteOperationMetadata>> PollOnceDeleteScheduleAsync(string operationName, CallSettings callSettings = null)

Asynchronously poll an operation once, using an `operationName` from a previous invocation of `DeleteSchedule`.

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
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Operation](https://docs.cloud.google.com/dotnet/docs/reference/Google.LongRunning/latest/Google.LongRunning.Operation-2.html)[Empty](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Empty.html)[DeleteOperationMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.DeleteOperationMetadata)` | A task representing the result of polling the operation.  
  
### ResumeSchedule(ResumeScheduleRequest, CallSettings)
    
    
    public virtual void ResumeSchedule(ResumeScheduleRequest request, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ResumeScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ResumeScheduleRequest request = new ResumeScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
        CatchUp = false,
    };
    // Make the request
    scheduleServiceClient.ResumeSchedule(request);
    

### ResumeSchedule(ScheduleName, CallSettings)
    
    
    public virtual void ResumeSchedule(ScheduleName name, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    scheduleServiceClient.ResumeSchedule(name);
    

### ResumeSchedule(ScheduleName, bool, CallSettings)
    
    
    public virtual void ResumeSchedule(ScheduleName name, bool catchUp, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`catchUp` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update [Schedule.catch_up][google.cloud.aiplatform.v1beta1.Schedule.catch_up] field. Default to false.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    bool catchUp = false;
    // Make the request
    scheduleServiceClient.ResumeSchedule(name, catchUp);
    

### ResumeSchedule(string, CallSettings)
    
    
    public virtual void ResumeSchedule(string name, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    scheduleServiceClient.ResumeSchedule(name);
    

### ResumeSchedule(string, bool, CallSettings)
    
    
    public virtual void ResumeSchedule(string name, bool catchUp, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`catchUp` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update [Schedule.catch_up][google.cloud.aiplatform.v1beta1.Schedule.catch_up] field. Default to false.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    bool catchUp = false;
    // Make the request
    scheduleServiceClient.ResumeSchedule(name, catchUp);
    

### ResumeScheduleAsync(ResumeScheduleRequest, CallSettings)
    
    
    public virtual Task ResumeScheduleAsync(ResumeScheduleRequest request, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ResumeScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ResumeScheduleRequest request = new ResumeScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
        CatchUp = false,
    };
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(request);
    

### ResumeScheduleAsync(ResumeScheduleRequest, CancellationToken)
    
    
    public virtual Task ResumeScheduleAsync(ResumeScheduleRequest request, CancellationToken cancellationToken)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ResumeScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ResumeScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ResumeScheduleRequest request = new ResumeScheduleRequest
    {
        ScheduleName = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]"),
        CatchUp = false,
    };
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(request);
    

### ResumeScheduleAsync(ScheduleName, CallSettings)
    
    
    public virtual Task ResumeScheduleAsync(ScheduleName name, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name);
    

### ResumeScheduleAsync(ScheduleName, bool, CallSettings)
    
    
    public virtual Task ResumeScheduleAsync(ScheduleName name, bool catchUp, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`catchUp` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update [Schedule.catch_up][google.cloud.aiplatform.v1beta1.Schedule.catch_up] field. Default to false.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    bool catchUp = false;
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name, catchUp);
    

### ResumeScheduleAsync(ScheduleName, bool, CancellationToken)
    
    
    public virtual Task ResumeScheduleAsync(ScheduleName name, bool catchUp, CancellationToken cancellationToken)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`catchUp` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update [Schedule.catch_up][google.cloud.aiplatform.v1beta1.Schedule.catch_up] field. Default to false.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    bool catchUp = false;
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name, catchUp);
    

### ResumeScheduleAsync(ScheduleName, CancellationToken)
    
    
    public virtual Task ResumeScheduleAsync(ScheduleName name, CancellationToken cancellationToken)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ScheduleName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleName)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    ScheduleName name = ScheduleName.FromProjectLocationSchedule("[PROJECT]", "[LOCATION]", "[SCHEDULE]");
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name);
    

### ResumeScheduleAsync(string, CallSettings)
    
    
    public virtual Task ResumeScheduleAsync(string name, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name);
    

### ResumeScheduleAsync(string, bool, CallSettings)
    
    
    public virtual Task ResumeScheduleAsync(string name, bool catchUp, CallSettings callSettings = null)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`catchUp` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update [Schedule.catch_up][google.cloud.aiplatform.v1beta1.Schedule.catch_up] field. Default to false.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    bool catchUp = false;
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name, catchUp);
    

### ResumeScheduleAsync(string, bool, CancellationToken)
    
    
    public virtual Task ResumeScheduleAsync(string name, bool catchUp, CancellationToken cancellationToken)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`catchUp` | `[bool](https://learn.microsoft.com/dotnet/api/system.boolean)`  
Optional. Whether to backfill missed runs when the schedule is resumed from PAUSED state. If set to true, all missed runs will be scheduled. New runs will be scheduled after the backfill is complete. This will also update [Schedule.catch_up][google.cloud.aiplatform.v1beta1.Schedule.catch_up] field. Default to false.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    bool catchUp = false;
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name, catchUp);
    

### ResumeScheduleAsync(string, CancellationToken)
    
    
    public virtual Task ResumeScheduleAsync(string name, CancellationToken cancellationToken)

Resumes a paused Schedule to start scheduling new runs. Will mark [Schedule.state][google.cloud.aiplatform.v1beta1.Schedule.state] to 'ACTIVE'. Only paused Schedule can be resumed.

When the Schedule is resumed, new runs will be scheduled starting from the next execution time after the current time based on the time_specification in the Schedule. If [Schedule.catchUp][] is set up true, all missed runs will be scheduled for backfill first.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the Schedule resource to be resumed. Format: `projects/{project}/locations/{location}/schedules/{schedule}`  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/locations/[LOCATION]/schedules/[SCHEDULE]";
    // Make the request
    await scheduleServiceClient.ResumeScheduleAsync(name);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient#Google_Cloud_AIPlatform_V1Beta1_ScheduleServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient#Google_Cloud_AIPlatform_V1Beta1_ScheduleServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient#Google_Cloud_AIPlatform_V1Beta1_ScheduleServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.ScheduleServiceClient#Google_Cloud_AIPlatform_V1Beta1_ScheduleServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### UpdateSchedule(Schedule, FieldMask, CallSettings)
    
    
    public virtual Schedule UpdateSchedule(Schedule schedule, FieldMask updateMask, CallSettings callSettings = null)

Updates an active or paused Schedule.

When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule which replaces the resource on the server. The following restrictions will be applied:

  * The scheduled request type cannot be changed.
  * The non-empty fields cannot be unset.
  * The output_only fields will be ignored if specified.

  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The update mask applies to the resource. See [google.protobuf.FieldMask][google.protobuf.FieldMask].  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    Schedule schedule = new Schedule();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Schedule response = scheduleServiceClient.UpdateSchedule(schedule, updateMask);
    

### UpdateSchedule(UpdateScheduleRequest, CallSettings)
    
    
    public virtual Schedule UpdateSchedule(UpdateScheduleRequest request, CallSettings callSettings = null)

Updates an active or paused Schedule.

When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | The RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = ScheduleServiceClient.Create();
    // Initialize request argument(s)
    UpdateScheduleRequest request = new UpdateScheduleRequest
    {
        Schedule = new Schedule(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Schedule response = scheduleServiceClient.UpdateSchedule(request);
    

### UpdateScheduleAsync(Schedule, FieldMask, CallSettings)
    
    
    public virtual Task<Schedule> UpdateScheduleAsync(Schedule schedule, FieldMask updateMask, CallSettings callSettings = null)

Updates an active or paused Schedule.

When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule which replaces the resource on the server. The following restrictions will be applied:

  * The scheduled request type cannot be changed.
  * The non-empty fields cannot be unset.
  * The output_only fields will be ignored if specified.

  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The update mask applies to the resource. See [google.protobuf.FieldMask][google.protobuf.FieldMask].  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    Schedule schedule = new Schedule();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Schedule response = await scheduleServiceClient.UpdateScheduleAsync(schedule, updateMask);
    

### UpdateScheduleAsync(Schedule, FieldMask, CancellationToken)
    
    
    public virtual Task<Schedule> UpdateScheduleAsync(Schedule schedule, FieldMask updateMask, CancellationToken cancellationToken)

Updates an active or paused Schedule.

When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`schedule` | `[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)`  
Required. The Schedule which replaces the resource on the server. The following restrictions will be applied:

  * The scheduled request type cannot be changed.
  * The non-empty fields cannot be unset.
  * The output_only fields will be ignored if specified.

  
`updateMask` | `[FieldMask](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.FieldMask.html)`  
Required. The update mask applies to the resource. See [google.protobuf.FieldMask][google.protobuf.FieldMask].  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    Schedule schedule = new Schedule();
    FieldMask updateMask = new FieldMask();
    // Make the request
    Schedule response = await scheduleServiceClient.UpdateScheduleAsync(schedule, updateMask);
    

### UpdateScheduleAsync(UpdateScheduleRequest, CallSettings)
    
    
    public virtual Task<Schedule> UpdateScheduleAsync(UpdateScheduleRequest request, CallSettings callSettings = null)

Updates an active or paused Schedule.

When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateScheduleRequest request = new UpdateScheduleRequest
    {
        Schedule = new Schedule(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Schedule response = await scheduleServiceClient.UpdateScheduleAsync(request);
    

### UpdateScheduleAsync(UpdateScheduleRequest, CancellationToken)
    
    
    public virtual Task<Schedule> UpdateScheduleAsync(UpdateScheduleRequest request, CancellationToken cancellationToken)

Updates an active or paused Schedule.

When the Schedule is updated, new runs will be scheduled starting from the updated next execution time after the update time based on the time_specification in the updated Schedule. All unstarted runs before the update time will be skipped while already created runs will NOT be paused or canceled.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[UpdateScheduleRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.UpdateScheduleRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Schedule](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.AIPlatform.V1Beta1/latest/Google.Cloud.AIPlatform.V1Beta1.Schedule)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ScheduleServiceClient scheduleServiceClient = await ScheduleServiceClient.CreateAsync();
    // Initialize request argument(s)
    UpdateScheduleRequest request = new UpdateScheduleRequest
    {
        Schedule = new Schedule(),
        UpdateMask = new FieldMask(),
    };
    // Make the request
    Schedule response = await scheduleServiceClient.UpdateScheduleAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
