---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient
title: Gemini Enterprise for Customer Experience v1beta API - Class WidgetServiceClient (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:46:47.766165+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class WidgetServiceClient (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class WidgetServiceClient (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public abstract class WidgetServiceClient

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class WidgetServiceClient.

WidgetService client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > WidgetServiceClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[WidgetServiceClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClientImpl)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Remarks

Provides APIs for widgets to interact with CES APIs.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the WidgetService service, which is a host of "ces.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default WidgetService scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default WidgetService scopes are:

  * <https://www.googleapis.com/auth/ces>
  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual WidgetService.WidgetServiceClient GrpcClient { get; }

The underlying gRPC WidgetService client

**Property Value**  
---  
**Type** | **Description**  
`[WidgetService](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetService)[WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetService.WidgetServiceClient)` |   
  
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
    
    
    public static WidgetServiceClient Create()

Synchronously creates a [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [WidgetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient)` | The created [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<WidgetServiceClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [WidgetServiceClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient)` | The task representing the created [WidgetServiceClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient).  
  
### GenerateChatToken(GenerateChatTokenRequest, CallSettings)
    
    
    public virtual GenerateChatTokenResponse GenerateChatToken(GenerateChatTokenRequest request, CallSettings callSettings = null)

Generates a session scoped token for chat widget to authenticate with Session APIs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateChatTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateChatTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    WidgetServiceClient widgetServiceClient = WidgetServiceClient.Create();
    // Initialize request argument(s)
    GenerateChatTokenRequest request = new GenerateChatTokenRequest
    {
        SessionName = SessionName.FromProjectLocationAppSession("[PROJECT]", "[LOCATION]", "[APP]", "[SESSION]"),
        DeploymentAsDeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
        RecaptchaToken = "",
        LiveHandoffEnabled = false,
    };
    // Make the request
    GenerateChatTokenResponse response = widgetServiceClient.GenerateChatToken(request);
    

### GenerateChatTokenAsync(GenerateChatTokenRequest, CallSettings)
    
    
    public virtual Task<GenerateChatTokenResponse> GenerateChatTokenAsync(GenerateChatTokenRequest request, CallSettings callSettings = null)

Generates a session scoped token for chat widget to authenticate with Session APIs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateChatTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateChatTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    WidgetServiceClient widgetServiceClient = await WidgetServiceClient.CreateAsync();
    // Initialize request argument(s)
    GenerateChatTokenRequest request = new GenerateChatTokenRequest
    {
        SessionName = SessionName.FromProjectLocationAppSession("[PROJECT]", "[LOCATION]", "[APP]", "[SESSION]"),
        DeploymentAsDeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
        RecaptchaToken = "",
        LiveHandoffEnabled = false,
    };
    // Make the request
    GenerateChatTokenResponse response = await widgetServiceClient.GenerateChatTokenAsync(request);
    

### GenerateChatTokenAsync(GenerateChatTokenRequest, CancellationToken)
    
    
    public virtual Task<GenerateChatTokenResponse> GenerateChatTokenAsync(GenerateChatTokenRequest request, CancellationToken cancellationToken)

Generates a session scoped token for chat widget to authenticate with Session APIs.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateChatTokenRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateChatTokenResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.GenerateChatTokenResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    WidgetServiceClient widgetServiceClient = await WidgetServiceClient.CreateAsync();
    // Initialize request argument(s)
    GenerateChatTokenRequest request = new GenerateChatTokenRequest
    {
        SessionName = SessionName.FromProjectLocationAppSession("[PROJECT]", "[LOCATION]", "[APP]", "[SESSION]"),
        DeploymentAsDeploymentName = DeploymentName.FromProjectLocationAppDeployment("[PROJECT]", "[LOCATION]", "[APP]", "[DEPLOYMENT]"),
        RecaptchaToken = "",
        LiveHandoffEnabled = false,
    };
    // Make the request
    GenerateChatTokenResponse response = await widgetServiceClient.GenerateChatTokenAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient#Google_Cloud_Ces_V1Beta_WidgetServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient#Google_Cloud_Ces_V1Beta_WidgetServiceClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient#Google_Cloud_Ces_V1Beta_WidgetServiceClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.WidgetServiceClient#Google_Cloud_Ces_V1Beta_WidgetServiceClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
