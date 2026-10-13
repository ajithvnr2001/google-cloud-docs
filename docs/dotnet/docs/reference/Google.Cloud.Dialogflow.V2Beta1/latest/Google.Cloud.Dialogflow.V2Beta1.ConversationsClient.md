---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient
title: Google Cloud Dialogflow v2beta1 API - Class ConversationsClient (1.0.0-beta33) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:10:33.215101+00:00
---

# Google Cloud Dialogflow v2beta1 API - Class ConversationsClient (1.0.0-beta33)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Dialogflow v2beta1 API - Class ConversationsClient (1.0.0-beta33) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta33 (latest)  1.0.0-beta32 
    
    
    public abstract class ConversationsClient

Reference documentation and code samples for the Google Cloud Dialogflow v2beta1 API class ConversationsClient.

Conversations client wrapper, for convenient use.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ConversationsClient

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Derived Types

[ConversationsClientImpl](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClientImpl)

## Namespace

[Google.Cloud.Dialogflow.V2Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1)

## Assembly

Google.Cloud.Dialogflow.V2Beta1.dll

## Remarks

Service for managing [Conversations][google.cloud.dialogflow.v2beta1.Conversation].

## Properties 

### DefaultEndpoint
    
    
    public static string DefaultEndpoint { get; }

The default endpoint for the Conversations service, which is a host of "dialogflow.googleapis.com" and a port of 443.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### DefaultScopes
    
    
    public static IReadOnlyList<string> DefaultScopes { get; }

The default Conversations scopes.

**Property Value**  
---  
**Type** | **Description**  
`[IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
**Remarks**

The default Conversations scopes are:

  * <https://www.googleapis.com/auth/cloud-platform>
  * <https://www.googleapis.com/auth/dialogflow>



### GrpcClient
    
    
    public virtual Conversations.ConversationsClient GrpcClient { get; }

The underlying gRPC Conversations client

**Property Value**  
---  
**Type** | **Description**  
`[Conversations](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversations)[ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversations.ConversationsClient)` |   
  
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

### BatchCreateMessages(BatchCreateMessagesRequest, CallSettings)
    
    
    public virtual BatchCreateMessagesResponse BatchCreateMessages(BatchCreateMessagesRequest request, CallSettings callSettings = null)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateMessagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    BatchCreateMessagesRequest request = new BatchCreateMessagesRequest
    {
        ParentAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        Requests =
        {
            new CreateMessageRequest(),
        },
    };
    // Make the request
    BatchCreateMessagesResponse response = conversationsClient.BatchCreateMessages(request);
    

### BatchCreateMessages(ConversationName, IEnumerable<CreateMessageRequest>, CallSettings)
    
    
    public virtual BatchCreateMessagesResponse BatchCreateMessages(ConversationName parent, IEnumerable<CreateMessageRequest> requests, CallSettings callSettings = null)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to create message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateMessageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateMessageRequest)`  
Required. A maximum of 300 messages can be created in a batch. [CreateMessageRequest.message.send_time][] is required. All created messages will have identical [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName parent = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    IEnumerable<CreateMessageRequest> requests = new CreateMessageRequest[]
    {
        new CreateMessageRequest(),
    };
    // Make the request
    BatchCreateMessagesResponse response = conversationsClient.BatchCreateMessages(parent, requests);
    

### BatchCreateMessages(string, IEnumerable<CreateMessageRequest>, CallSettings)
    
    
    public virtual BatchCreateMessagesResponse BatchCreateMessages(string parent, IEnumerable<CreateMessageRequest> requests, CallSettings callSettings = null)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to create message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateMessageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateMessageRequest)`  
Required. A maximum of 300 messages can be created in a batch. [CreateMessageRequest.message.send_time][] is required. All created messages will have identical [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/conversations/[CONVERSATION]";
    IEnumerable<CreateMessageRequest> requests = new CreateMessageRequest[]
    {
        new CreateMessageRequest(),
    };
    // Make the request
    BatchCreateMessagesResponse response = conversationsClient.BatchCreateMessages(parent, requests);
    

### BatchCreateMessagesAsync(BatchCreateMessagesRequest, CallSettings)
    
    
    public virtual Task<BatchCreateMessagesResponse> BatchCreateMessagesAsync(BatchCreateMessagesRequest request, CallSettings callSettings = null)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateMessagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    BatchCreateMessagesRequest request = new BatchCreateMessagesRequest
    {
        ParentAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        Requests =
        {
            new CreateMessageRequest(),
        },
    };
    // Make the request
    BatchCreateMessagesResponse response = await conversationsClient.BatchCreateMessagesAsync(request);
    

### BatchCreateMessagesAsync(BatchCreateMessagesRequest, CancellationToken)
    
    
    public virtual Task<BatchCreateMessagesResponse> BatchCreateMessagesAsync(BatchCreateMessagesRequest request, CancellationToken cancellationToken)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[BatchCreateMessagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    BatchCreateMessagesRequest request = new BatchCreateMessagesRequest
    {
        ParentAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        Requests =
        {
            new CreateMessageRequest(),
        },
    };
    // Make the request
    BatchCreateMessagesResponse response = await conversationsClient.BatchCreateMessagesAsync(request);
    

### BatchCreateMessagesAsync(ConversationName, IEnumerable<CreateMessageRequest>, CallSettings)
    
    
    public virtual Task<BatchCreateMessagesResponse> BatchCreateMessagesAsync(ConversationName parent, IEnumerable<CreateMessageRequest> requests, CallSettings callSettings = null)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to create message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateMessageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateMessageRequest)`  
Required. A maximum of 300 messages can be created in a batch. [CreateMessageRequest.message.send_time][] is required. All created messages will have identical [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName parent = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    IEnumerable<CreateMessageRequest> requests = new CreateMessageRequest[]
    {
        new CreateMessageRequest(),
    };
    // Make the request
    BatchCreateMessagesResponse response = await conversationsClient.BatchCreateMessagesAsync(parent, requests);
    

### BatchCreateMessagesAsync(ConversationName, IEnumerable<CreateMessageRequest>, CancellationToken)
    
    
    public virtual Task<BatchCreateMessagesResponse> BatchCreateMessagesAsync(ConversationName parent, IEnumerable<CreateMessageRequest> requests, CancellationToken cancellationToken)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to create message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateMessageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateMessageRequest)`  
Required. A maximum of 300 messages can be created in a batch. [CreateMessageRequest.message.send_time][] is required. All created messages will have identical [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName parent = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    IEnumerable<CreateMessageRequest> requests = new CreateMessageRequest[]
    {
        new CreateMessageRequest(),
    };
    // Make the request
    BatchCreateMessagesResponse response = await conversationsClient.BatchCreateMessagesAsync(parent, requests);
    

### BatchCreateMessagesAsync(string, IEnumerable<CreateMessageRequest>, CallSettings)
    
    
    public virtual Task<BatchCreateMessagesResponse> BatchCreateMessagesAsync(string parent, IEnumerable<CreateMessageRequest> requests, CallSettings callSettings = null)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to create message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateMessageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateMessageRequest)`  
Required. A maximum of 300 messages can be created in a batch. [CreateMessageRequest.message.send_time][] is required. All created messages will have identical [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/conversations/[CONVERSATION]";
    IEnumerable<CreateMessageRequest> requests = new CreateMessageRequest[]
    {
        new CreateMessageRequest(),
    };
    // Make the request
    BatchCreateMessagesResponse response = await conversationsClient.BatchCreateMessagesAsync(parent, requests);
    

### BatchCreateMessagesAsync(string, IEnumerable<CreateMessageRequest>, CancellationToken)
    
    
    public virtual Task<BatchCreateMessagesResponse> BatchCreateMessagesAsync(string parent, IEnumerable<CreateMessageRequest> requests, CancellationToken cancellationToken)

Batch ingests messages to conversation. Customers can use this RPC to ingest historical messages to conversation.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to create message. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`requests` | `[IEnumerable](https://learn.microsoft.com/dotnet/api/system.collections.generic.ienumerable-1)[CreateMessageRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateMessageRequest)`  
Required. A maximum of 300 messages can be created in a batch. [CreateMessageRequest.message.send_time][] is required. All created messages will have identical [Message.create_time][google.cloud.dialogflow.v2beta1.Message.create_time].  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[BatchCreateMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.BatchCreateMessagesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/conversations/[CONVERSATION]";
    IEnumerable<CreateMessageRequest> requests = new CreateMessageRequest[]
    {
        new CreateMessageRequest(),
    };
    // Make the request
    BatchCreateMessagesResponse response = await conversationsClient.BatchCreateMessagesAsync(parent, requests);
    

### CompleteConversation(CompleteConversationRequest, CallSettings)
    
    
    public virtual Conversation CompleteConversation(CompleteConversationRequest request, CallSettings callSettings = null)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CompleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    CompleteConversationRequest request = new CompleteConversationRequest
    {
        ConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = conversationsClient.CompleteConversation(request);
    

### CompleteConversation(ConversationName, CallSettings)
    
    
    public virtual Conversation CompleteConversation(ConversationName name, CallSettings callSettings = null)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    Conversation response = conversationsClient.CompleteConversation(name);
    

### CompleteConversation(string, CallSettings)
    
    
    public virtual Conversation CompleteConversation(string name, CallSettings callSettings = null)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = conversationsClient.CompleteConversation(name);
    

### CompleteConversationAsync(CompleteConversationRequest, CallSettings)
    
    
    public virtual Task<Conversation> CompleteConversationAsync(CompleteConversationRequest request, CallSettings callSettings = null)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CompleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    CompleteConversationRequest request = new CompleteConversationRequest
    {
        ConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = await conversationsClient.CompleteConversationAsync(request);
    

### CompleteConversationAsync(CompleteConversationRequest, CancellationToken)
    
    
    public virtual Task<Conversation> CompleteConversationAsync(CompleteConversationRequest request, CancellationToken cancellationToken)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CompleteConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CompleteConversationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    CompleteConversationRequest request = new CompleteConversationRequest
    {
        ConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = await conversationsClient.CompleteConversationAsync(request);
    

### CompleteConversationAsync(ConversationName, CallSettings)
    
    
    public virtual Task<Conversation> CompleteConversationAsync(ConversationName name, CallSettings callSettings = null)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    Conversation response = await conversationsClient.CompleteConversationAsync(name);
    

### CompleteConversationAsync(ConversationName, CancellationToken)
    
    
    public virtual Task<Conversation> CompleteConversationAsync(ConversationName name, CancellationToken cancellationToken)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    Conversation response = await conversationsClient.CompleteConversationAsync(name);
    

### CompleteConversationAsync(string, CallSettings)
    
    
    public virtual Task<Conversation> CompleteConversationAsync(string name, CallSettings callSettings = null)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = await conversationsClient.CompleteConversationAsync(name);
    

### CompleteConversationAsync(string, CancellationToken)
    
    
    public virtual Task<Conversation> CompleteConversationAsync(string name, CancellationToken cancellationToken)

Completes the specified conversation. Finished conversations are purged from the database after 30 days.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to close. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = await conversationsClient.CompleteConversationAsync(name);
    

### Create()
    
    
    public static ConversationsClient Create()

Synchronously creates a [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ConversationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClientBuilder).

**Returns**  
---  
**Type** | **Description**  
`[ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient)` | The created [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient).  
  
### CreateAsync(CancellationToken)
    
    
    public static Task<ConversationsClient> CreateAsync(CancellationToken cancellationToken = default)

Asynchronously creates a [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient) using the default credentials, endpoint and settings. To specify custom credentials or other settings, use [ConversationsClientBuilder](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClientBuilder).

**Parameter**  
---  
**Name** | **Description**  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
The [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use while creating the client.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient)` | The task representing the created [ConversationsClient](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient).  
  
### CreateConversation(LocationName, Conversation, CallSettings)
    
    
    public virtual Conversation CreateConversation(LocationName parent, Conversation conversation, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = conversationsClient.CreateConversation(parent, conversation);
    

### CreateConversation(ProjectName, Conversation, CallSettings)
    
    
    public virtual Conversation CreateConversation(ProjectName parent, Conversation conversation, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = conversationsClient.CreateConversation(parent, conversation);
    

### CreateConversation(CreateConversationRequest, CallSettings)
    
    
    public virtual Conversation CreateConversation(CreateConversationRequest request, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    CreateConversationRequest request = new CreateConversationRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Conversation = new Conversation(),
        ConversationId = "",
    };
    // Make the request
    Conversation response = conversationsClient.CreateConversation(request);
    

### CreateConversation(string, Conversation, CallSettings)
    
    
    public virtual Conversation CreateConversation(string parent, Conversation conversation, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = conversationsClient.CreateConversation(parent, conversation);
    

### CreateConversationAsync(LocationName, Conversation, CallSettings)
    
    
    public virtual Task<Conversation> CreateConversationAsync(LocationName parent, Conversation conversation, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(parent, conversation);
    

### CreateConversationAsync(LocationName, Conversation, CancellationToken)
    
    
    public virtual Task<Conversation> CreateConversationAsync(LocationName parent, Conversation conversation, CancellationToken cancellationToken)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(parent, conversation);
    

### CreateConversationAsync(ProjectName, Conversation, CallSettings)
    
    
    public virtual Task<Conversation> CreateConversationAsync(ProjectName parent, Conversation conversation, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(parent, conversation);
    

### CreateConversationAsync(ProjectName, Conversation, CancellationToken)
    
    
    public virtual Task<Conversation> CreateConversationAsync(ProjectName parent, Conversation conversation, CancellationToken cancellationToken)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(parent, conversation);
    

### CreateConversationAsync(CreateConversationRequest, CallSettings)
    
    
    public virtual Task<Conversation> CreateConversationAsync(CreateConversationRequest request, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    CreateConversationRequest request = new CreateConversationRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Conversation = new Conversation(),
        ConversationId = "",
    };
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(request);
    

### CreateConversationAsync(CreateConversationRequest, CancellationToken)
    
    
    public virtual Task<Conversation> CreateConversationAsync(CreateConversationRequest request, CancellationToken cancellationToken)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[CreateConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.CreateConversationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    CreateConversationRequest request = new CreateConversationRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Conversation = new Conversation(),
        ConversationId = "",
    };
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(request);
    

### CreateConversationAsync(string, Conversation, CallSettings)
    
    
    public virtual Task<Conversation> CreateConversationAsync(string parent, Conversation conversation, CallSettings callSettings = null)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(parent, conversation);
    

### CreateConversationAsync(string, Conversation, CancellationToken)
    
    
    public virtual Task<Conversation> CreateConversationAsync(string parent, Conversation conversation, CancellationToken cancellationToken)

Creates a new conversation. Conversations are auto-completed after 24 hours.

Conversation Lifecycle: There are two stages during a conversation: Automated Agent Stage and Assist Stage.

For Automated Agent Stage, there will be a dialogflow agent responding to user queries.

For Assist Stage, there's no dialogflow agent responding to user queries. But we will provide suggestions which are generated from conversation.

If [Conversation.conversation_profile][google.cloud.dialogflow.v2beta1.Conversation.conversation_profile] is configured for a dialogflow agent, conversation will start from `Automated Agent Stage`, otherwise, it will start from `Assist Stage`. And during `Automated Agent Stage`, once an [Intent][google.cloud.dialogflow.v2beta1.Intent] with [Intent.live_agent_handoff][google.cloud.dialogflow.v2beta1.Intent.live_agent_handoff] is triggered, conversation will transfer to Assist Stage.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the project creating the conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`conversation` | `[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)`  
Required. The conversation to create.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    Conversation conversation = new Conversation();
    // Make the request
    Conversation response = await conversationsClient.CreateConversationAsync(parent, conversation);
    

### GenerateStatelessSuggestion(GenerateStatelessSuggestionRequest, CallSettings)
    
    
    public virtual GenerateStatelessSuggestionResponse GenerateStatelessSuggestion(GenerateStatelessSuggestionRequest request, CallSettings callSettings = null)

Generates and returns a suggestion for a conversation that does not have a resource created for it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSuggestionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSuggestionResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    GenerateStatelessSuggestionRequest request = new GenerateStatelessSuggestionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Generator = new Generator(),
        ContextReferences =
        {
            {
                "",
                new Conversation.Types.ContextReference()
            },
        },
        ConversationContext = new ConversationContext(),
        TriggerEvents =
        {
            TriggerEvent.Unspecified,
        },
        SecuritySettings = "",
    };
    // Make the request
    GenerateStatelessSuggestionResponse response = conversationsClient.GenerateStatelessSuggestion(request);
    

### GenerateStatelessSuggestionAsync(GenerateStatelessSuggestionRequest, CallSettings)
    
    
    public virtual Task<GenerateStatelessSuggestionResponse> GenerateStatelessSuggestionAsync(GenerateStatelessSuggestionRequest request, CallSettings callSettings = null)

Generates and returns a suggestion for a conversation that does not have a resource created for it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSuggestionRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSuggestionResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GenerateStatelessSuggestionRequest request = new GenerateStatelessSuggestionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Generator = new Generator(),
        ContextReferences =
        {
            {
                "",
                new Conversation.Types.ContextReference()
            },
        },
        ConversationContext = new ConversationContext(),
        TriggerEvents =
        {
            TriggerEvent.Unspecified,
        },
        SecuritySettings = "",
    };
    // Make the request
    GenerateStatelessSuggestionResponse response = await conversationsClient.GenerateStatelessSuggestionAsync(request);
    

### GenerateStatelessSuggestionAsync(GenerateStatelessSuggestionRequest, CancellationToken)
    
    
    public virtual Task<GenerateStatelessSuggestionResponse> GenerateStatelessSuggestionAsync(GenerateStatelessSuggestionRequest request, CancellationToken cancellationToken)

Generates and returns a suggestion for a conversation that does not have a resource created for it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSuggestionRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSuggestionRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateStatelessSuggestionResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSuggestionResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GenerateStatelessSuggestionRequest request = new GenerateStatelessSuggestionRequest
    {
        ParentAsLocationName = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]"),
        Generator = new Generator(),
        ContextReferences =
        {
            {
                "",
                new Conversation.Types.ContextReference()
            },
        },
        ConversationContext = new ConversationContext(),
        TriggerEvents =
        {
            TriggerEvent.Unspecified,
        },
        SecuritySettings = "",
    };
    // Make the request
    GenerateStatelessSuggestionResponse response = await conversationsClient.GenerateStatelessSuggestionAsync(request);
    

### GenerateStatelessSummary(GenerateStatelessSummaryRequest, CallSettings)
    
    
    public virtual GenerateStatelessSummaryResponse GenerateStatelessSummary(GenerateStatelessSummaryRequest request, CallSettings callSettings = null)

Generates and returns a summary for a conversation that does not have a resource created for it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSummaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateStatelessSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSummaryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    GenerateStatelessSummaryRequest request = new GenerateStatelessSummaryRequest
    {
        StatelessConversation = new GenerateStatelessSummaryRequest.Types.MinimalConversation(),
        ConversationProfile = new ConversationProfile(),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        MaxContextSize = 0,
    };
    // Make the request
    GenerateStatelessSummaryResponse response = conversationsClient.GenerateStatelessSummary(request);
    

### GenerateStatelessSummaryAsync(GenerateStatelessSummaryRequest, CallSettings)
    
    
    public virtual Task<GenerateStatelessSummaryResponse> GenerateStatelessSummaryAsync(GenerateStatelessSummaryRequest request, CallSettings callSettings = null)

Generates and returns a summary for a conversation that does not have a resource created for it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSummaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateStatelessSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GenerateStatelessSummaryRequest request = new GenerateStatelessSummaryRequest
    {
        StatelessConversation = new GenerateStatelessSummaryRequest.Types.MinimalConversation(),
        ConversationProfile = new ConversationProfile(),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        MaxContextSize = 0,
    };
    // Make the request
    GenerateStatelessSummaryResponse response = await conversationsClient.GenerateStatelessSummaryAsync(request);
    

### GenerateStatelessSummaryAsync(GenerateStatelessSummaryRequest, CancellationToken)
    
    
    public virtual Task<GenerateStatelessSummaryResponse> GenerateStatelessSummaryAsync(GenerateStatelessSummaryRequest request, CancellationToken cancellationToken)

Generates and returns a summary for a conversation that does not have a resource created for it.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateStatelessSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSummaryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateStatelessSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateStatelessSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GenerateStatelessSummaryRequest request = new GenerateStatelessSummaryRequest
    {
        StatelessConversation = new GenerateStatelessSummaryRequest.Types.MinimalConversation(),
        ConversationProfile = new ConversationProfile(),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        MaxContextSize = 0,
    };
    // Make the request
    GenerateStatelessSummaryResponse response = await conversationsClient.GenerateStatelessSummaryAsync(request);
    

### GenerateSuggestions(ConversationName, CallSettings)
    
    
    public virtual GenerateSuggestionsResponse GenerateSuggestions(ConversationName conversation, CallSettings callSettings = null)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    GenerateSuggestionsResponse response = conversationsClient.GenerateSuggestions(conversation);
    

### GenerateSuggestions(GenerateSuggestionsRequest, CallSettings)
    
    
    public virtual GenerateSuggestionsResponse GenerateSuggestions(GenerateSuggestionsRequest request, CallSettings callSettings = null)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    GenerateSuggestionsRequest request = new GenerateSuggestionsRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        TriggerEvents =
        {
            TriggerEvent.Unspecified,
        },
    };
    // Make the request
    GenerateSuggestionsResponse response = conversationsClient.GenerateSuggestions(request);
    

### GenerateSuggestions(string, CallSettings)
    
    
    public virtual GenerateSuggestionsResponse GenerateSuggestions(string conversation, CallSettings callSettings = null)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    GenerateSuggestionsResponse response = conversationsClient.GenerateSuggestions(conversation);
    

### GenerateSuggestionsAsync(ConversationName, CallSettings)
    
    
    public virtual Task<GenerateSuggestionsResponse> GenerateSuggestionsAsync(ConversationName conversation, CallSettings callSettings = null)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    GenerateSuggestionsResponse response = await conversationsClient.GenerateSuggestionsAsync(conversation);
    

### GenerateSuggestionsAsync(ConversationName, CancellationToken)
    
    
    public virtual Task<GenerateSuggestionsResponse> GenerateSuggestionsAsync(ConversationName conversation, CancellationToken cancellationToken)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    GenerateSuggestionsResponse response = await conversationsClient.GenerateSuggestionsAsync(conversation);
    

### GenerateSuggestionsAsync(GenerateSuggestionsRequest, CallSettings)
    
    
    public virtual Task<GenerateSuggestionsResponse> GenerateSuggestionsAsync(GenerateSuggestionsRequest request, CallSettings callSettings = null)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GenerateSuggestionsRequest request = new GenerateSuggestionsRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        TriggerEvents =
        {
            TriggerEvent.Unspecified,
        },
    };
    // Make the request
    GenerateSuggestionsResponse response = await conversationsClient.GenerateSuggestionsAsync(request);
    

### GenerateSuggestionsAsync(GenerateSuggestionsRequest, CancellationToken)
    
    
    public virtual Task<GenerateSuggestionsResponse> GenerateSuggestionsAsync(GenerateSuggestionsRequest request, CancellationToken cancellationToken)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GenerateSuggestionsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GenerateSuggestionsRequest request = new GenerateSuggestionsRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        TriggerEvents =
        {
            TriggerEvent.Unspecified,
        },
    };
    // Make the request
    GenerateSuggestionsResponse response = await conversationsClient.GenerateSuggestionsAsync(request);
    

### GenerateSuggestionsAsync(string, CallSettings)
    
    
    public virtual Task<GenerateSuggestionsResponse> GenerateSuggestionsAsync(string conversation, CallSettings callSettings = null)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    GenerateSuggestionsResponse response = await conversationsClient.GenerateSuggestionsAsync(conversation);
    

### GenerateSuggestionsAsync(string, CancellationToken)
    
    
    public virtual Task<GenerateSuggestionsResponse> GenerateSuggestionsAsync(string conversation, CancellationToken cancellationToken)

Generates all the suggestions using generators configured in the conversation profile. A generator is used only if its trigger event is matched.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The conversation for which the suggestions are generated. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`. The conversation must be created with a conversation profile which has generators configured in it to be able to get suggestions.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[GenerateSuggestionsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GenerateSuggestionsResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    GenerateSuggestionsResponse response = await conversationsClient.GenerateSuggestionsAsync(conversation);
    

### GetConversation(ConversationName, CallSettings)
    
    
    public virtual Conversation GetConversation(ConversationName name, CallSettings callSettings = null)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    Conversation response = conversationsClient.GetConversation(name);
    

### GetConversation(GetConversationRequest, CallSettings)
    
    
    public virtual Conversation GetConversation(GetConversationRequest request, CallSettings callSettings = null)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    GetConversationRequest request = new GetConversationRequest
    {
        ConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = conversationsClient.GetConversation(request);
    

### GetConversation(string, CallSettings)
    
    
    public virtual Conversation GetConversation(string name, CallSettings callSettings = null)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = conversationsClient.GetConversation(name);
    

### GetConversationAsync(ConversationName, CallSettings)
    
    
    public virtual Task<Conversation> GetConversationAsync(ConversationName name, CallSettings callSettings = null)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    Conversation response = await conversationsClient.GetConversationAsync(name);
    

### GetConversationAsync(ConversationName, CancellationToken)
    
    
    public virtual Task<Conversation> GetConversationAsync(ConversationName name, CancellationToken cancellationToken)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName name = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    Conversation response = await conversationsClient.GetConversationAsync(name);
    

### GetConversationAsync(GetConversationRequest, CallSettings)
    
    
    public virtual Task<Conversation> GetConversationAsync(GetConversationRequest request, CallSettings callSettings = null)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GetConversationRequest request = new GetConversationRequest
    {
        ConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = await conversationsClient.GetConversationAsync(request);
    

### GetConversationAsync(GetConversationRequest, CancellationToken)
    
    
    public virtual Task<Conversation> GetConversationAsync(GetConversationRequest request, CancellationToken cancellationToken)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[GetConversationRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.GetConversationRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    GetConversationRequest request = new GetConversationRequest
    {
        ConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
    };
    // Make the request
    Conversation response = await conversationsClient.GetConversationAsync(request);
    

### GetConversationAsync(string, CallSettings)
    
    
    public virtual Task<Conversation> GetConversationAsync(string name, CallSettings callSettings = null)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = await conversationsClient.GetConversationAsync(name);
    

### GetConversationAsync(string, CancellationToken)
    
    
    public virtual Task<Conversation> GetConversationAsync(string name, CancellationToken cancellationToken)

Retrieves the specific conversation.

**Parameters**  
---  
**Name** | **Description**  
`name` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the conversation. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string name = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    Conversation response = await conversationsClient.GetConversationAsync(name);
    

### IngestContextReferences(ConversationName, IDictionary<string, ContextReference>, CallSettings)
    
    
    public virtual IngestContextReferencesResponse IngestContextReferences(ConversationName conversation, IDictionary<string, Conversation.Types.ContextReference> contextReferences, CallSettings callSettings = null)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    IDictionary<string, Conversation.Types.ContextReference> contextReferences = new Dictionary<string, Conversation.Types.ContextReference>
    {
        {
            "",
            new Conversation.Types.ContextReference()
        },
    };
    // Make the request
    IngestContextReferencesResponse response = conversationsClient.IngestContextReferences(conversation, contextReferences);
    

### IngestContextReferences(IngestContextReferencesRequest, CallSettings)
    
    
    public virtual IngestContextReferencesResponse IngestContextReferences(IngestContextReferencesRequest request, CallSettings callSettings = null)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IngestContextReferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    IngestContextReferencesRequest request = new IngestContextReferencesRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        ContextReferences =
        {
            {
                "",
                new Conversation.Types.ContextReference()
            },
        },
    };
    // Make the request
    IngestContextReferencesResponse response = conversationsClient.IngestContextReferences(request);
    

### IngestContextReferences(string, IDictionary<string, ContextReference>, CallSettings)
    
    
    public virtual IngestContextReferencesResponse IngestContextReferences(string conversation, IDictionary<string, Conversation.Types.ContextReference> contextReferences, CallSettings callSettings = null)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    IDictionary<string, Conversation.Types.ContextReference> contextReferences = new Dictionary<string, Conversation.Types.ContextReference>
    {
        {
            "",
            new Conversation.Types.ContextReference()
        },
    };
    // Make the request
    IngestContextReferencesResponse response = conversationsClient.IngestContextReferences(conversation, contextReferences);
    

### IngestContextReferencesAsync(ConversationName, IDictionary<string, ContextReference>, CallSettings)
    
    
    public virtual Task<IngestContextReferencesResponse> IngestContextReferencesAsync(ConversationName conversation, IDictionary<string, Conversation.Types.ContextReference> contextReferences, CallSettings callSettings = null)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    IDictionary<string, Conversation.Types.ContextReference> contextReferences = new Dictionary<string, Conversation.Types.ContextReference>
    {
        {
            "",
            new Conversation.Types.ContextReference()
        },
    };
    // Make the request
    IngestContextReferencesResponse response = await conversationsClient.IngestContextReferencesAsync(conversation, contextReferences);
    

### IngestContextReferencesAsync(ConversationName, IDictionary<string, ContextReference>, CancellationToken)
    
    
    public virtual Task<IngestContextReferencesResponse> IngestContextReferencesAsync(ConversationName conversation, IDictionary<string, Conversation.Types.ContextReference> contextReferences, CancellationToken cancellationToken)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    IDictionary<string, Conversation.Types.ContextReference> contextReferences = new Dictionary<string, Conversation.Types.ContextReference>
    {
        {
            "",
            new Conversation.Types.ContextReference()
        },
    };
    // Make the request
    IngestContextReferencesResponse response = await conversationsClient.IngestContextReferencesAsync(conversation, contextReferences);
    

### IngestContextReferencesAsync(IngestContextReferencesRequest, CallSettings)
    
    
    public virtual Task<IngestContextReferencesResponse> IngestContextReferencesAsync(IngestContextReferencesRequest request, CallSettings callSettings = null)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IngestContextReferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    IngestContextReferencesRequest request = new IngestContextReferencesRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        ContextReferences =
        {
            {
                "",
                new Conversation.Types.ContextReference()
            },
        },
    };
    // Make the request
    IngestContextReferencesResponse response = await conversationsClient.IngestContextReferencesAsync(request);
    

### IngestContextReferencesAsync(IngestContextReferencesRequest, CancellationToken)
    
    
    public virtual Task<IngestContextReferencesResponse> IngestContextReferencesAsync(IngestContextReferencesRequest request, CancellationToken cancellationToken)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[IngestContextReferencesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    IngestContextReferencesRequest request = new IngestContextReferencesRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        ContextReferences =
        {
            {
                "",
                new Conversation.Types.ContextReference()
            },
        },
    };
    // Make the request
    IngestContextReferencesResponse response = await conversationsClient.IngestContextReferencesAsync(request);
    

### IngestContextReferencesAsync(string, IDictionary<string, ContextReference>, CallSettings)
    
    
    public virtual Task<IngestContextReferencesResponse> IngestContextReferencesAsync(string conversation, IDictionary<string, Conversation.Types.ContextReference> contextReferences, CallSettings callSettings = null)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    IDictionary<string, Conversation.Types.ContextReference> contextReferences = new Dictionary<string, Conversation.Types.ContextReference>
    {
        {
            "",
            new Conversation.Types.ContextReference()
        },
    };
    // Make the request
    IngestContextReferencesResponse response = await conversationsClient.IngestContextReferencesAsync(conversation, contextReferences);
    

### IngestContextReferencesAsync(string, IDictionary<string, ContextReference>, CancellationToken)
    
    
    public virtual Task<IngestContextReferencesResponse> IngestContextReferencesAsync(string conversation, IDictionary<string, Conversation.Types.ContextReference> contextReferences, CancellationToken cancellationToken)

Data ingestion API. Ingests context references for an existing conversation.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. Resource identifier of the conversation to ingest context information for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`contextReferences` | `[IDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.idictionary-2)[string](https://learn.microsoft.com/dotnet/api/system.string)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types)[ContextReference](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation.Types.ContextReference)`  
Required. The context references to ingest. The key is the name of the context reference and the value contains the contents of the context reference. The key is used to incorporate ingested context references to enhance the generator.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[IngestContextReferencesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.IngestContextReferencesResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    IDictionary<string, Conversation.Types.ContextReference> contextReferences = new Dictionary<string, Conversation.Types.ContextReference>
    {
        {
            "",
            new Conversation.Types.ContextReference()
        },
    };
    // Make the request
    IngestContextReferencesResponse response = await conversationsClient.IngestContextReferencesAsync(conversation, contextReferences);
    

### ListConversations(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversations(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversations(ListConversationsRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(ListConversationsRequest request, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ListConversationsRequest request = new ListConversationsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversations(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversations(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListConversationsResponse, Conversation> ListConversations(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversations(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(LocationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(LocationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[LocationName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.LocationName.html)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    LocationName parent = LocationName.FromProjectLocation("[PROJECT]", "[LOCATION]");
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(ProjectName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(ProjectName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ProjectName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.ResourceNames.ProjectName.html)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ProjectName parent = ProjectName.FromProject("[PROJECT]");
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(ListConversationsRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(ListConversationsRequest request, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListConversationsRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ListConversationsRequest request = new ListConversationsRequest
    {
        ParentAsProjectName = ProjectName.FromProject("[PROJECT]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversationsAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListConversationsAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListConversationsResponse, Conversation> ListConversationsAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Returns the list of all conversations in the specified project.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The project from which to list all conversation. Format: `projects/<Project ID>/locations/<Location ID>`.  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListConversationsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListConversationsResponse)[Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation)` | A pageable asynchronous sequence of [Conversation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Conversation) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]";
    // Make the request
    PagedAsyncEnumerable<ListConversationsResponse, Conversation> response = conversationsClient.ListConversationsAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Conversation item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListConversationsResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Conversation item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Conversation> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Conversation item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMessages(ConversationName, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMessagesResponse, Message> ListMessages(ConversationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The name of the conversation to list messages for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesResponse)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message)` | A pageable sequence of [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName parent = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    PagedEnumerable<ListMessagesResponse, Message> response = conversationsClient.ListMessages(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Message item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMessagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Message item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Message> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Message item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMessages(ListMessagesRequest, CallSettings)
    
    
    public virtual PagedEnumerable<ListMessagesResponse, Message> ListMessages(ListMessagesRequest request, CallSettings callSettings = null)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMessagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesResponse)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message)` | A pageable sequence of [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ListMessagesRequest request = new ListMessagesRequest
    {
        ParentAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        Filter = "",
    };
    // Make the request
    PagedEnumerable<ListMessagesResponse, Message> response = conversationsClient.ListMessages(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Message item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMessagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Message item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Message> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Message item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMessages(string, string, int?, CallSettings)
    
    
    public virtual PagedEnumerable<ListMessagesResponse, Message> ListMessages(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the conversation to list messages for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedEnumerable-2.html)[ListMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesResponse)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message)` | A pageable sequence of [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    PagedEnumerable<ListMessagesResponse, Message> response = conversationsClient.ListMessages(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    foreach (Message item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    foreach (ListMessagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Message item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Message> singlePage = response.ReadPage(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Message item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMessagesAsync(ConversationName, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMessagesResponse, Message> ListMessagesAsync(ConversationName parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The name of the conversation to list messages for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesResponse)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message)` | A pageable asynchronous sequence of [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName parent = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    PagedAsyncEnumerable<ListMessagesResponse, Message> response = conversationsClient.ListMessagesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Message item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMessagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Message item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Message> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Message item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMessagesAsync(ListMessagesRequest, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMessagesResponse, Message> ListMessagesAsync(ListMessagesRequest request, CallSettings callSettings = null)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[ListMessagesRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesResponse)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message)` | A pageable asynchronous sequence of [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ListMessagesRequest request = new ListMessagesRequest
    {
        ParentAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        Filter = "",
    };
    // Make the request
    PagedAsyncEnumerable<ListMessagesResponse, Message> response = conversationsClient.ListMessagesAsync(request);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Message item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMessagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Message item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Message> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Message item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### ListMessagesAsync(string, string, int?, CallSettings)
    
    
    public virtual PagedAsyncEnumerable<ListMessagesResponse, Message> ListMessagesAsync(string parent, string pageToken = null, int? pageSize = null, CallSettings callSettings = null)

Lists messages that belong to a given conversation. `messages` are ordered by `create_time` in descending order. To fetch updates without duplication, send request with filter `create_time_epoch_microseconds > [first item's create_time of previous request]` and empty page_token.

**Parameters**  
---  
**Name** | **Description**  
`parent` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The name of the conversation to list messages for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`  
`pageToken` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
The token returned from the previous request. A value of `null` or an empty string retrieves the first page.  
`pageSize` | `[int](https://learn.microsoft.com/dotnet/api/system.int32)`  
The size of page to request. The response will not be larger than this, but may be smaller. A value of `null` or `0` uses a server-defined page size.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[PagedAsyncEnumerable](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.PagedAsyncEnumerable-2.html)[ListMessagesResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ListMessagesResponse)[Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message)` | A pageable asynchronous sequence of [Message](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.Message) resources.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string parent = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    PagedAsyncEnumerable<ListMessagesResponse, Message> response = conversationsClient.ListMessagesAsync(parent);
    
    // Iterate over all response items, lazily performing RPCs as required
    await foreach (Message item in response)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    
    // Or iterate over pages (of server-defined size), performing one RPC per page
    await foreach (ListMessagesResponse page in response.AsRawResponses())
    {
        // Do something with each page of items
        Console.WriteLine("A page of results:");
        foreach (Message item in page)
        {
            // Do something with each item
            Console.WriteLine(item);
        }
    }
    
    // Or retrieve a single page of known size (unless it's the final page), performing as many RPCs as required
    int pageSize = 10;
    Page<Message> singlePage = await response.ReadPageAsync(pageSize);
    // Do something with the page of items
    Console.WriteLine($"A page of {pageSize} results (unless it's the final page):");
    foreach (Message item in singlePage)
    {
        // Do something with each item
        Console.WriteLine(item);
    }
    // Store the pageToken, for when the next page is required.
    string nextPageToken = singlePage.NextPageToken;
    

### SearchKnowledge(SearchKnowledgeRequest, CallSettings)
    
    
    public virtual SearchKnowledgeResponse SearchKnowledge(SearchKnowledgeRequest request, CallSettings callSettings = null)

Get answers for the given query based on knowledge documents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchKnowledgeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SearchKnowledgeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SearchKnowledgeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SearchKnowledgeResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    SearchKnowledgeRequest request = new SearchKnowledgeRequest
    {
        Query = new TextInput(),
        ConversationProfileAsConversationProfileName = ConversationProfileName.FromProjectConversationProfile("[PROJECT]", "[CONVERSATION_PROFILE]"),
        SessionId = "",
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        Parent = "",
        QuerySource = SearchKnowledgeRequest.Types.QuerySource.Unspecified,
        EndUserMetadata = new Struct(),
        SearchConfig = new SearchKnowledgeRequest.Types.SearchConfig(),
        ExactSearch = false,
    };
    // Make the request
    SearchKnowledgeResponse response = conversationsClient.SearchKnowledge(request);
    

### SearchKnowledgeAsync(SearchKnowledgeRequest, CallSettings)
    
    
    public virtual Task<SearchKnowledgeResponse> SearchKnowledgeAsync(SearchKnowledgeRequest request, CallSettings callSettings = null)

Get answers for the given query based on knowledge documents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchKnowledgeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SearchKnowledgeRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchKnowledgeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SearchKnowledgeResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    SearchKnowledgeRequest request = new SearchKnowledgeRequest
    {
        Query = new TextInput(),
        ConversationProfileAsConversationProfileName = ConversationProfileName.FromProjectConversationProfile("[PROJECT]", "[CONVERSATION_PROFILE]"),
        SessionId = "",
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        Parent = "",
        QuerySource = SearchKnowledgeRequest.Types.QuerySource.Unspecified,
        EndUserMetadata = new Struct(),
        SearchConfig = new SearchKnowledgeRequest.Types.SearchConfig(),
        ExactSearch = false,
    };
    // Make the request
    SearchKnowledgeResponse response = await conversationsClient.SearchKnowledgeAsync(request);
    

### SearchKnowledgeAsync(SearchKnowledgeRequest, CancellationToken)
    
    
    public virtual Task<SearchKnowledgeResponse> SearchKnowledgeAsync(SearchKnowledgeRequest request, CancellationToken cancellationToken)

Get answers for the given query based on knowledge documents.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SearchKnowledgeRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SearchKnowledgeRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SearchKnowledgeResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SearchKnowledgeResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    SearchKnowledgeRequest request = new SearchKnowledgeRequest
    {
        Query = new TextInput(),
        ConversationProfileAsConversationProfileName = ConversationProfileName.FromProjectConversationProfile("[PROJECT]", "[CONVERSATION_PROFILE]"),
        SessionId = "",
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        Parent = "",
        QuerySource = SearchKnowledgeRequest.Types.QuerySource.Unspecified,
        EndUserMetadata = new Struct(),
        SearchConfig = new SearchKnowledgeRequest.Types.SearchConfig(),
        ExactSearch = false,
    };
    // Make the request
    SearchKnowledgeResponse response = await conversationsClient.SearchKnowledgeAsync(request);
    

### ShutdownDefaultChannelsAsync()
    
    
    public static Task ShutdownDefaultChannelsAsync()

Shuts down any channels automatically created by [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient#Google_Cloud_Dialogflow_V2Beta1_ConversationsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient#Google_Cloud_Dialogflow_V2Beta1_ConversationsClient_CreateAsync_System_Threading_CancellationToken_). Channels which weren't automatically created are not affected.

**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)` | A task representing the asynchronous shutdown operation.  
**Remarks**

After calling this method, further calls to [Create()](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient#Google_Cloud_Dialogflow_V2Beta1_ConversationsClient_Create) and [CreateAsync(CancellationToken)](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationsClient#Google_Cloud_Dialogflow_V2Beta1_ConversationsClient_CreateAsync_System_Threading_CancellationToken_) will create new channels, which could in turn be shut down by another call to this method.

### SuggestConversationSummary(ConversationName, CallSettings)
    
    
    public virtual SuggestConversationSummaryResponse SuggestConversationSummary(ConversationName conversation, CallSettings callSettings = null)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    SuggestConversationSummaryResponse response = conversationsClient.SuggestConversationSummary(conversation);
    

### SuggestConversationSummary(SuggestConversationSummaryRequest, CallSettings)
    
    
    public virtual SuggestConversationSummaryResponse SuggestConversationSummary(SuggestConversationSummaryRequest request, CallSettings callSettings = null)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestConversationSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    SuggestConversationSummaryRequest request = new SuggestConversationSummaryRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        ContextSize = 0,
        AssistQueryParams = new AssistQueryParameters(),
    };
    // Make the request
    SuggestConversationSummaryResponse response = conversationsClient.SuggestConversationSummary(request);
    

### SuggestConversationSummary(string, CallSettings)
    
    
    public virtual SuggestConversationSummaryResponse SuggestConversationSummary(string conversation, CallSettings callSettings = null)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | The RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = ConversationsClient.Create();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    SuggestConversationSummaryResponse response = conversationsClient.SuggestConversationSummary(conversation);
    

### SuggestConversationSummaryAsync(ConversationName, CallSettings)
    
    
    public virtual Task<SuggestConversationSummaryResponse> SuggestConversationSummaryAsync(ConversationName conversation, CallSettings callSettings = null)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    SuggestConversationSummaryResponse response = await conversationsClient.SuggestConversationSummaryAsync(conversation);
    

### SuggestConversationSummaryAsync(ConversationName, CancellationToken)
    
    
    public virtual Task<SuggestConversationSummaryResponse> SuggestConversationSummaryAsync(ConversationName conversation, CancellationToken cancellationToken)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[ConversationName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.ConversationName)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    ConversationName conversation = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]");
    // Make the request
    SuggestConversationSummaryResponse response = await conversationsClient.SuggestConversationSummaryAsync(conversation);
    

### SuggestConversationSummaryAsync(SuggestConversationSummaryRequest, CallSettings)
    
    
    public virtual Task<SuggestConversationSummaryResponse> SuggestConversationSummaryAsync(SuggestConversationSummaryRequest request, CallSettings callSettings = null)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestConversationSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryRequest)`  
The request object containing all of the parameters for the API call.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    SuggestConversationSummaryRequest request = new SuggestConversationSummaryRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        ContextSize = 0,
        AssistQueryParams = new AssistQueryParameters(),
    };
    // Make the request
    SuggestConversationSummaryResponse response = await conversationsClient.SuggestConversationSummaryAsync(request);
    

### SuggestConversationSummaryAsync(SuggestConversationSummaryRequest, CancellationToken)
    
    
    public virtual Task<SuggestConversationSummaryResponse> SuggestConversationSummaryAsync(SuggestConversationSummaryRequest request, CancellationToken cancellationToken)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`request` | `[SuggestConversationSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryRequest)`  
The request object containing all of the parameters for the API call.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    SuggestConversationSummaryRequest request = new SuggestConversationSummaryRequest
    {
        ConversationAsConversationName = ConversationName.FromProjectConversation("[PROJECT]", "[CONVERSATION]"),
        LatestMessageAsMessageName = MessageName.FromProjectConversationMessage("[PROJECT]", "[CONVERSATION]", "[MESSAGE]"),
        ContextSize = 0,
        AssistQueryParams = new AssistQueryParameters(),
    };
    // Make the request
    SuggestConversationSummaryResponse response = await conversationsClient.SuggestConversationSummaryAsync(request);
    

### SuggestConversationSummaryAsync(string, CallSettings)
    
    
    public virtual Task<SuggestConversationSummaryResponse> SuggestConversationSummaryAsync(string conversation, CallSettings callSettings = null)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`callSettings` | `[CallSettings](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.Grpc.CallSettings.html)`  
If not null, applies overrides to this RPC call.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    SuggestConversationSummaryResponse response = await conversationsClient.SuggestConversationSummaryAsync(conversation);
    

### SuggestConversationSummaryAsync(string, CancellationToken)
    
    
    public virtual Task<SuggestConversationSummaryResponse> SuggestConversationSummaryAsync(string conversation, CancellationToken cancellationToken)

Suggest summary for a conversation based on specific historical messages. The range of the messages to be used for summary can be specified in the request.

**Parameters**  
---  
**Name** | **Description**  
`conversation` | `[string](https://learn.microsoft.com/dotnet/api/system.string)`  
Required. The conversation to fetch suggestion for. Format: `projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>`.  
`cancellationToken` | `[CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken)`  
A [CancellationToken](https://learn.microsoft.com/dotnet/api/system.threading.cancellationtoken) to use for this RPC.  
**Returns**  
---  
**Type** | **Description**  
`[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task-1)[SuggestConversationSummaryResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Dialogflow.V2Beta1/latest/Google.Cloud.Dialogflow.V2Beta1.SuggestConversationSummaryResponse)` | A Task containing the RPC response.  
**Example**
    
    
    // Create client
    ConversationsClient conversationsClient = await ConversationsClient.CreateAsync();
    // Initialize request argument(s)
    string conversation = "projects/[PROJECT]/conversations/[CONVERSATION]";
    // Make the request
    SuggestConversationSummaryResponse response = await conversationsClient.SuggestConversationSummaryAsync(conversation);
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
