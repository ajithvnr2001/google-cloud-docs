---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient
title: Policy Troubleshooter v1 API - Class IamCheckerClient (2.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:20:52.862897+00:00
---

# Policy Troubleshooter v1 API - Class IamCheckerClient (2.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Policy Troubleshooter v1 API - Class IamCheckerClient (2.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/2.5.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/2.4.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/2.3.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/2.2.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/2.1.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/2.0.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/1.2.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/1.1.0/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)


    
    
    public abstract class IamCheckerClient

Reference documentation and code samples for the Policy Troubleshooter v1 API class IamCheckerClient.

IamChecker client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > IamCheckerClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[IamCheckerClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClientImpl)

## Namespace

[Google.Cloud.PolicyTroubleshooter.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1)

## Assembly

Google.Cloud.PolicyTroubleshooter.V1.dll

## Remarks

IAM Policy Troubleshooter service.

This service helps you troubleshoot access issues for Google Cloud resources.

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the IamChecker service, which is a host of "policytroubleshooter.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default IamChecker scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default IamChecker scopes are: 

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual IamChecker.IamCheckerClient GrpcClient { get; }

The underlying gRPC IamChecker client

**Property Value**  
---  
**Type** | **Description**  
`[IamChecker](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamChecker)[IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamChecker.IamCheckerClient)` |   
  
### ServiceMetadata
    
    
    public static ServiceMetadata ServiceMetadata { get; }

The service metadata associated with this client type.

**Property Value**  
---  
**Type** | **Description**  
`[ServiceMetadata](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.ServiceMetadata.html)` |   
  
## Methods 

### Create()
    
    
    public static IamCheckerClient Create()

Synchronously creates a [IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [IamCheckerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)` | The created [IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<IamCheckerClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [IamCheckerClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient)` | The task representing the created [IamCheckerClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient).  
  
### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient#Google_Cloud_PolicyTroubleshooter_V1_IamCheckerClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient#Google_Cloud_PolicyTroubleshooter_V1_IamCheckerClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient#Google_Cloud_PolicyTroubleshooter_V1_IamCheckerClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.IamCheckerClient#Google_Cloud_PolicyTroubleshooter_V1_IamCheckerClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### TroubleshootIamPolicy(TroubleshootIamPolicyRequest, CallSettings)
    
    
    public virtual TroubleshootIamPolicyResponse TroubleshootIamPolicy(TroubleshootIamPolicyRequest request, CallSettings callSettings = null)

Checks whether a principal has a specific permission for a specific resource, and explains why the principal does or does not have that permission.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TroubleshootIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.TroubleshootIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[TroubleshootIamPolicyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.TroubleshootIamPolicyResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    IamCheckerClient iamCheckerClient = IamCheckerClient.Create();
    // Initialize request argument(s)
    TroubleshootIamPolicyRequest request = new TroubleshootIamPolicyRequest
    {
        AccessTuple = new AccessTuple(),
    };
    // Make the request
    TroubleshootIamPolicyResponse response = iamCheckerClient.TroubleshootIamPolicy(request);
    

### TroubleshootIamPolicyAsync(TroubleshootIamPolicyRequest, CallSettings)
    
    
    public virtual Task<TroubleshootIamPolicyResponse> TroubleshootIamPolicyAsync(TroubleshootIamPolicyRequest request, CallSettings callSettings = null)

Checks whether a principal has a specific permission for a specific resource, and explains why the principal does or does not have that permission.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TroubleshootIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.TroubleshootIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TroubleshootIamPolicyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.TroubleshootIamPolicyResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IamCheckerClient iamCheckerClient = await IamCheckerClient.CreateAsync();
    // Initialize request argument(s)
    TroubleshootIamPolicyRequest request = new TroubleshootIamPolicyRequest
    {
        AccessTuple = new AccessTuple(),
    };
    // Make the request
    TroubleshootIamPolicyResponse response = await iamCheckerClient.TroubleshootIamPolicyAsync(request);
    

### TroubleshootIamPolicyAsync(TroubleshootIamPolicyRequest, CancellationToken)
    
    
    public virtual Task<TroubleshootIamPolicyResponse> TroubleshootIamPolicyAsync(TroubleshootIamPolicyRequest request, CancellationToken cancellationToken)

Checks whether a principal has a specific permission for a specific resource, and explains why the principal does or does not have that permission.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[TroubleshootIamPolicyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.TroubleshootIamPolicyRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[TroubleshootIamPolicyResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.PolicyTroubleshooter.V1/latest/Google.Cloud.PolicyTroubleshooter.V1.TroubleshootIamPolicyResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    IamCheckerClient iamCheckerClient = await IamCheckerClient.CreateAsync();
    // Initialize request argument(s)
    TroubleshootIamPolicyRequest request = new TroubleshootIamPolicyRequest
    {
        AccessTuple = new AccessTuple(),
    };
    // Make the request
    TroubleshootIamPolicyResponse response = await iamCheckerClient.TroubleshootIamPolicyAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
