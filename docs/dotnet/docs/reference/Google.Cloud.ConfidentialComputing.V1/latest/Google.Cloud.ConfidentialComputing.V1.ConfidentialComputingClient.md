---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient
title: Confidential Computing v1 API - Class ConfidentialComputingClient (1.13.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:54:17.133501+00:00
---

# Confidential Computing v1 API - Class ConfidentialComputingClient (1.13.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Confidential Computing v1 API - Class ConfidentialComputingClient (1.13.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.13.0 (latest)  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0 
    
    
    public abstract class ConfidentialComputingClient

Reference documentation and code samples for the Confidential Computing v1 API class ConfidentialComputingClient.

ConfidentialComputing client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConfidentialComputingClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ConfidentialComputingClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClientImpl)

## Namespace

[Google.Cloud.ConfidentialComputing.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1)

## Assembly

Google.Cloud.ConfidentialComputing.V1.dll

## Remarks

Service describing handlers for resources

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the ConfidentialComputing service, which is a host of "confidentialcomputing.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default ConfidentialComputing scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default ConfidentialComputing scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>



### GrpcClient
    
    
    public virtual ConfidentialComputing.ConfidentialComputingClient GrpcClient { get; }

The underlying gRPC ConfidentialComputing client

**Property Value**  
---  
**Type** | **Description**  
`[ConfidentialComputing](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputing)[ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputing.ConfidentialComputingClient)` |   
  
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
    
    
    public static ConfidentialComputingClient Create()

Synchronously creates a [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ConfidentialComputingClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient)` | The created [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ConfidentialComputingClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ConfidentialComputingClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient)` | The task representing the created [ConfidentialComputingClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient).  
  
### CreateChallenge(LocationName, Challenge, CallSettings)
    
    
    public virtual Challenge CreateChallenge(LocationName parent, Challenge challenge, CallSettings callSettings = null)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location where the Challenge will be used, in the format `projects/*/locations/*`.  
`challenge` | `[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)`  
Required. The Challenge to be created. Currently this field can be empty as all the Challenge fields are set by the server.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | The RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = ConfidentialComputingClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Challenge challenge = new Challenge();
    // Make the request
    Challenge response = confidentialComputingClient.CreateChallenge(parent, challenge);
    

### CreateChallenge(CreateChallengeRequest, CallSettings)
    
    
    public virtual Challenge CreateChallenge(CreateChallengeRequest request, CallSettings callSettings = null)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateChallengeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.CreateChallengeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | The RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = ConfidentialComputingClient.Create();
    // Initialize request argument(s)
    CreateChallengeRequest request = new CreateChallengeRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Challenge = new Challenge(),
    };
    // Make the request
    Challenge response = confidentialComputingClient.CreateChallenge(request);
    

### CreateChallenge(string, Challenge, CallSettings)
    
    
    public virtual Challenge CreateChallenge(string parent, Challenge challenge, CallSettings callSettings = null)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location where the Challenge will be used, in the format `projects/*/locations/*`.  
`challenge` | `[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)`  
Required. The Challenge to be created. Currently this field can be empty as all the Challenge fields are set by the server.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | The RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = ConfidentialComputingClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Challenge challenge = new Challenge();
    // Make the request
    Challenge response = confidentialComputingClient.CreateChallenge(parent, challenge);
    

### CreateChallengeAsync(LocationName, Challenge, CallSettings)
    
    
    public virtual Task<Challenge> CreateChallengeAsync(LocationName parent, Challenge challenge, CallSettings callSettings = null)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location where the Challenge will be used, in the format `projects/*/locations/*`.  
`challenge` | `[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)`  
Required. The Challenge to be created. Currently this field can be empty as all the Challenge fields are set by the server.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Challenge challenge = new Challenge();
    // Make the request
    Challenge response = await confidentialComputingClient.CreateChallengeAsync(parent, challenge);
    

### CreateChallengeAsync(LocationName, Challenge, CancellationToken)
    
    
    public virtual Task<Challenge> CreateChallengeAsync(LocationName parent, Challenge challenge, CancellationToken cancellationToken)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The resource name of the location where the Challenge will be used, in the format `projects/*/locations/*`.  
`challenge` | `[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)`  
Required. The Challenge to be created. Currently this field can be empty as all the Challenge fields are set by the server.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Challenge challenge = new Challenge();
    // Make the request
    Challenge response = await confidentialComputingClient.CreateChallengeAsync(parent, challenge);
    

### CreateChallengeAsync(CreateChallengeRequest, CallSettings)
    
    
    public virtual Task<Challenge> CreateChallengeAsync(CreateChallengeRequest request, CallSettings callSettings = null)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateChallengeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.CreateChallengeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    CreateChallengeRequest request = new CreateChallengeRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Challenge = new Challenge(),
    };
    // Make the request
    Challenge response = await confidentialComputingClient.CreateChallengeAsync(request);
    

### CreateChallengeAsync(CreateChallengeRequest, CancellationToken)
    
    
    public virtual Task<Challenge> CreateChallengeAsync(CreateChallengeRequest request, CancellationToken cancellationToken)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateChallengeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.CreateChallengeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    CreateChallengeRequest request = new CreateChallengeRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Challenge = new Challenge(),
    };
    // Make the request
    Challenge response = await confidentialComputingClient.CreateChallengeAsync(request);
    

### CreateChallengeAsync(string, Challenge, CallSettings)
    
    
    public virtual Task<Challenge> CreateChallengeAsync(string parent, Challenge challenge, CallSettings callSettings = null)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location where the Challenge will be used, in the format `projects/*/locations/*`.  
`challenge` | `[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)`  
Required. The Challenge to be created. Currently this field can be empty as all the Challenge fields are set by the server.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Challenge challenge = new Challenge();
    // Make the request
    Challenge response = await confidentialComputingClient.CreateChallengeAsync(parent, challenge);
    

### CreateChallengeAsync(string, Challenge, CancellationToken)
    
    
    public virtual Task<Challenge> CreateChallengeAsync(string parent, Challenge challenge, CancellationToken cancellationToken)

Creates a new Challenge in a given project and location.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The resource name of the location where the Challenge will be used, in the format `projects/*/locations/*`.  
`challenge` | `[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)`  
Required. The Challenge to be created. Currently this field can be empty as all the Challenge fields are set by the server.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Challenge](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.Challenge)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/locations/[LOCATION]";
    Challenge challenge = new Challenge();
    // Make the request
    Challenge response = await confidentialComputingClient.CreateChallengeAsync(parent, challenge);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient#Google_Cloud_ConfidentialComputing_V1_ConfidentialComputingClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient#Google_Cloud_ConfidentialComputing_V1_ConfidentialComputingClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient#Google_Cloud_ConfidentialComputing_V1_ConfidentialComputingClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.ConfidentialComputingClient#Google_Cloud_ConfidentialComputing_V1_ConfidentialComputingClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### VerifyAttestation(VerifyAttestationRequest, CallSettings)
    
    
    public virtual VerifyAttestationResponse VerifyAttestation(VerifyAttestationRequest request, CallSettings callSettings = null)

Verifies the provided attestation info, returning a signed attestation token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyAttestationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[VerifyAttestationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = ConfidentialComputingClient.Create();
    // Initialize request argument(s)
    VerifyAttestationRequest request = new VerifyAttestationRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        GcpCredentials = new GcpCredentials(),
        TpmAttestation = new TpmAttestation(),
        ConfidentialSpaceInfo = new ConfidentialSpaceInfo(),
        TokenOptions = new TokenOptions(),
        TdCcel = new TdxCcelAttestation(),
        Attester = "",
        NvidiaAttestation = new NvidiaAttestation(),
        InstanceAsInstanceName = InstanceName.FromProjectZoneInstance("[PROJECT]", "[ZONE]", "[INSTANCE]"),
    };
    // Make the request
    VerifyAttestationResponse response = confidentialComputingClient.VerifyAttestation(request);
    

### VerifyAttestationAsync(VerifyAttestationRequest, CallSettings)
    
    
    public virtual Task<VerifyAttestationResponse> VerifyAttestationAsync(VerifyAttestationRequest request, CallSettings callSettings = null)

Verifies the provided attestation info, returning a signed attestation token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyAttestationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyAttestationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    VerifyAttestationRequest request = new VerifyAttestationRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        GcpCredentials = new GcpCredentials(),
        TpmAttestation = new TpmAttestation(),
        ConfidentialSpaceInfo = new ConfidentialSpaceInfo(),
        TokenOptions = new TokenOptions(),
        TdCcel = new TdxCcelAttestation(),
        Attester = "",
        NvidiaAttestation = new NvidiaAttestation(),
        InstanceAsInstanceName = InstanceName.FromProjectZoneInstance("[PROJECT]", "[ZONE]", "[INSTANCE]"),
    };
    // Make the request
    VerifyAttestationResponse response = await confidentialComputingClient.VerifyAttestationAsync(request);
    

### VerifyAttestationAsync(VerifyAttestationRequest, CancellationToken)
    
    
    public virtual Task<VerifyAttestationResponse> VerifyAttestationAsync(VerifyAttestationRequest request, CancellationToken cancellationToken)

Verifies the provided attestation info, returning a signed attestation token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyAttestationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyAttestationResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyAttestationResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    VerifyAttestationRequest request = new VerifyAttestationRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        GcpCredentials = new GcpCredentials(),
        TpmAttestation = new TpmAttestation(),
        ConfidentialSpaceInfo = new ConfidentialSpaceInfo(),
        TokenOptions = new TokenOptions(),
        TdCcel = new TdxCcelAttestation(),
        Attester = "",
        NvidiaAttestation = new NvidiaAttestation(),
        InstanceAsInstanceName = InstanceName.FromProjectZoneInstance("[PROJECT]", "[ZONE]", "[INSTANCE]"),
    };
    // Make the request
    VerifyAttestationResponse response = await confidentialComputingClient.VerifyAttestationAsync(request);
    

### VerifyConfidentialGke(VerifyConfidentialGkeRequest, CallSettings)
    
    
    public virtual VerifyConfidentialGkeResponse VerifyConfidentialGke(VerifyConfidentialGkeRequest request, CallSettings callSettings = null)

Verifies the provided Confidential GKE attestation info, returning a signed OIDC token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialGkeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialGkeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = ConfidentialComputingClient.Create();
    // Initialize request argument(s)
    VerifyConfidentialGkeRequest request = new VerifyConfidentialGkeRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        TpmAttestation = new TpmAttestation(),
        Options = new VerifyConfidentialGkeRequest.Types.ConfidentialGkeOptions(),
        PlatformType = VerifyConfidentialGkeRequest.Types.PlatformType.Unspecified,
    };
    // Make the request
    VerifyConfidentialGkeResponse response = confidentialComputingClient.VerifyConfidentialGke(request);
    

### VerifyConfidentialGkeAsync(VerifyConfidentialGkeRequest, CallSettings)
    
    
    public virtual Task<VerifyConfidentialGkeResponse> VerifyConfidentialGkeAsync(VerifyConfidentialGkeRequest request, CallSettings callSettings = null)

Verifies the provided Confidential GKE attestation info, returning a signed OIDC token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialGkeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyConfidentialGkeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    VerifyConfidentialGkeRequest request = new VerifyConfidentialGkeRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        TpmAttestation = new TpmAttestation(),
        Options = new VerifyConfidentialGkeRequest.Types.ConfidentialGkeOptions(),
        PlatformType = VerifyConfidentialGkeRequest.Types.PlatformType.Unspecified,
    };
    // Make the request
    VerifyConfidentialGkeResponse response = await confidentialComputingClient.VerifyConfidentialGkeAsync(request);
    

### VerifyConfidentialGkeAsync(VerifyConfidentialGkeRequest, CancellationToken)
    
    
    public virtual Task<VerifyConfidentialGkeResponse> VerifyConfidentialGkeAsync(VerifyConfidentialGkeRequest request, CancellationToken cancellationToken)

Verifies the provided Confidential GKE attestation info, returning a signed OIDC token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialGkeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyConfidentialGkeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialGkeResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    VerifyConfidentialGkeRequest request = new VerifyConfidentialGkeRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        TpmAttestation = new TpmAttestation(),
        Options = new VerifyConfidentialGkeRequest.Types.ConfidentialGkeOptions(),
        PlatformType = VerifyConfidentialGkeRequest.Types.PlatformType.Unspecified,
    };
    // Make the request
    VerifyConfidentialGkeResponse response = await confidentialComputingClient.VerifyConfidentialGkeAsync(request);
    

### VerifyConfidentialSpace(VerifyConfidentialSpaceRequest, CallSettings)
    
    
    public virtual VerifyConfidentialSpaceResponse VerifyConfidentialSpace(VerifyConfidentialSpaceRequest request, CallSettings callSettings = null)

Verifies whether the provided attestation info is valid, returning a signed attestation token if so.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[VerifyConfidentialSpaceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = ConfidentialComputingClient.Create();
    // Initialize request argument(s)
    VerifyConfidentialSpaceRequest request = new VerifyConfidentialSpaceRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        GcpCredentials = new GcpCredentials(),
        TdCcel = new TdxCcelAttestation(),
        SignedEntities = { new SignedEntity(), },
        GceShieldedIdentity = new GceShieldedIdentity(),
        Options = new VerifyConfidentialSpaceRequest.Types.ConfidentialSpaceOptions(),
        NvidiaAttestation = new NvidiaAttestation(),
    };
    // Make the request
    VerifyConfidentialSpaceResponse response = confidentialComputingClient.VerifyConfidentialSpace(request);
    

### VerifyConfidentialSpaceAsync(VerifyConfidentialSpaceRequest, CallSettings)
    
    
    public virtual Task<VerifyConfidentialSpaceResponse> VerifyConfidentialSpaceAsync(VerifyConfidentialSpaceRequest request, CallSettings callSettings = null)

Verifies whether the provided attestation info is valid, returning a signed attestation token if so.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyConfidentialSpaceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    VerifyConfidentialSpaceRequest request = new VerifyConfidentialSpaceRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        GcpCredentials = new GcpCredentials(),
        TdCcel = new TdxCcelAttestation(),
        SignedEntities = { new SignedEntity(), },
        GceShieldedIdentity = new GceShieldedIdentity(),
        Options = new VerifyConfidentialSpaceRequest.Types.ConfidentialSpaceOptions(),
        NvidiaAttestation = new NvidiaAttestation(),
    };
    // Make the request
    VerifyConfidentialSpaceResponse response = await confidentialComputingClient.VerifyConfidentialSpaceAsync(request);
    

### VerifyConfidentialSpaceAsync(VerifyConfidentialSpaceRequest, CancellationToken)
    
    
    public virtual Task<VerifyConfidentialSpaceResponse> VerifyConfidentialSpaceAsync(VerifyConfidentialSpaceRequest request, CancellationToken cancellationToken)

Verifies whether the provided attestation info is valid, returning a signed attestation token if so.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[VerifyConfidentialSpaceRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[VerifyConfidentialSpaceResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.ConfidentialComputing.V1/latest/Google.Cloud.ConfidentialComputing.V1.VerifyConfidentialSpaceResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConfidentialComputingClient confidentialComputingClient = await ConfidentialComputingClient.CreateAsync();
    // Initialize request argument(s)
    VerifyConfidentialSpaceRequest request = new VerifyConfidentialSpaceRequest
    {
        ChallengeAsChallengeName = ChallengeName.FromProjectLocationUuid("[PROJECT]", "[LOCATION]", "[UUID]"),
        GcpCredentials = new GcpCredentials(),
        TdCcel = new TdxCcelAttestation(),
        SignedEntities = { new SignedEntity(), },
        GceShieldedIdentity = new GceShieldedIdentity(),
        Options = new VerifyConfidentialSpaceRequest.Types.ConfidentialSpaceOptions(),
        NvidiaAttestation = new NvidiaAttestation(),
    };
    // Make the request
    VerifyConfidentialSpaceResponse response = await confidentialComputingClient.VerifyConfidentialSpaceAsync(request);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
